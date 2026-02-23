#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Radar-ANPR Detections JSON to CAMWIM VirtualTicket Mapper

Reads detection JSON files from the detections/ folder (created by radaranprvms.py),
maps them to VirtualTicket format, and posts to the CAMWIM Service.
Runs continuously: polls for new detections, sends unsent data, marks sent records.
Images are skipped (no lpImageFrontBase64, lpImageBackBase64, overviewImagesBase64).
"""

import json
import logging
import os
import requests
import time
import uuid
from datetime import datetime, date

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('datamapper_detections_json.log')
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# CONFIGURATION
# ============================================================================

DETECTIONS_FOLDER = "detections"
CAMWIM_SERVICE_URL = "http://89.24.183.108:4040"
CAMWIM_ENHANCED_ENDPOINT = "/api/VirtualTicket/enhanced"
CAMWIM_PROGRESS_ENDPOINT = "/api/DataImportProgress"

BATCH_SIZE = 50
MAX_RETRIES = 3
RETRY_DELAY = 5
SENT_STATE_FILE = 'datamapper_sent_state.json'  # Tracks (file, index) - only reads files with new data
POLL_INTERVAL = 15  # Seconds between checks for new detections


# ============================================================================
# PROGRESS TRACKER
# ============================================================================

class DataImportProgressTracker:
    """Handles progress tracking with the CAMWIM Service backend"""

    def __init__(self, service_url):
        self.service_url = service_url
        self.import_id = None
        self.progress_endpoint = f"{service_url}{CAMWIM_PROGRESS_ENDPOINT}"

    def start_import(self, description, first_record_id, last_record_id):
        """Start a new import operation"""
        self.import_id = str(uuid.uuid4())
        payload = {
            "importId": self.import_id,
            "description": description,
            "firstRecordId": first_record_id,
            "lastRecordId": last_record_id
        }
        try:
            response = requests.post(f"{self.progress_endpoint}/start", json=payload, timeout=30)
            if response.status_code == 200:
                logger.info(f"Started import operation: {self.import_id}")
                return True
            else:
                logger.error(f"Failed to start import: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            logger.error(f"Error starting import: {e}")
            return False

    def update_progress(self, last_processed_id, processed_count, failed_count=0):
        """Update the progress of the import operation"""
        if not self.import_id:
            return False
        payload = {
            "lastProcessedId": last_processed_id,
            "processedCount": processed_count,
            "failedCount": failed_count
        }
        try:
            response = requests.put(f"{self.progress_endpoint}/{self.import_id}/progress", json=payload, timeout=30)
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error updating progress: {e}")
            return False

    def complete_import(self, processed_count, failed_count=0):
        """Complete the import operation"""
        if not self.import_id:
            return False
        payload = {"processedCount": processed_count, "failedCount": failed_count}
        try:
            response = requests.put(f"{self.progress_endpoint}/{self.import_id}/complete", json=payload, timeout=30)
            if response.status_code == 200:
                logger.info(f"Completed import operation: {self.import_id}")
                return True
            else:
                logger.error(f"Failed to complete import: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            logger.error(f"Error completing import: {e}")
            return False

    def fail_import(self, error_message):
        """Mark the import operation as failed"""
        if not self.import_id:
            return False
        payload = {"errorMessage": error_message}
        try:
            response = requests.put(f"{self.progress_endpoint}/{self.import_id}/fail", json=payload, timeout=30)
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error failing import: {e}")
            return False

    def get_progress(self):
        """Get the current progress of the import operation"""
        if not self.import_id:
            return None
        try:
            response = requests.get(f"{self.progress_endpoint}/{self.import_id}", timeout=30)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            logger.error(f"Error getting progress: {e}")
            return None


# ============================================================================
# FILE READING
# ============================================================================

def get_detection_json_files(folder=DETECTIONS_FOLDER):
    """Get sorted list of detection JSON files (DD_MM_YYYY.json)"""
    if not os.path.exists(folder):
        logger.warning(f"Detections folder does not exist: {folder}")
        return []
    files = []
    for f in os.listdir(folder):
        if f.endswith('.json') and len(f) == 12:  # DD_MM_YYYY.json
            path = os.path.join(folder, f)
            if os.path.isfile(path):
                files.append(path)
    files.sort()
    return files


def load_detections_from_file(filepath, retries=3):
    """Load detections list from a JSON file. Retries on decode error (file may be mid-write)."""
    for attempt in range(retries):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
        except json.JSONDecodeError as e:
            if attempt < retries - 1:
                time.sleep(0.5)
                continue
            logger.error(f"Invalid JSON in {filepath}: {e}")
            return []
        except IOError as e:
            logger.error(f"Error reading {filepath}: {e}")
            return []
    return []


# ============================================================================
# MAPPING: Detection JSON -> VirtualTicket
# ============================================================================

def map_detection_to_virtual_ticket(detection, record_id):
    """
    Map a radar/ANPR detection to VirtualTicket format.
    Detection fields: timestamp, plate_number, speed, direction, radar_direction_sign,
    vms_displayed, radar_readings_count, radar_detection_start, radar_detection_end.
    Images are skipped (empty).
    """
    timestamp = detection.get('timestamp')
    if isinstance(timestamp, str):
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            date_time_local = dt.strftime('%Y-%m-%dT%H:%M:%S')
        except (ValueError, TypeError):
            date_time_local = timestamp or ''
    else:
        date_time_local = str(timestamp) if timestamp else ''

    plate = detection.get('plate_number') or ''
    speed = detection.get('speed') or 0

    virtual_ticket = {
        "ticketId": record_id,
        "cid": record_id,
        "dateTimeLocal": date_time_local,
        "wim": detection.get('direction', '') or '',
        "vehicleClass": "unknown",
        "velocity": float(speed) if speed is not None else 0,
        "length": 0,
        "licensePlate": plate,
        "anprAssist": None,
        "licensePlateBack": None,
        "totalWeight": 0,
        "axlesCount": 0,
        "axleConf": "",
        "permissible": 0,
        "avw": 0,
        "gvw": 0,
        "overweighting": "0" * 20,
        "dualTire": "0" * 18,
        "carLayout": "1+1",
        "axleOverloadNo": 0,
        "tagged": 0,
        "exported": 0,
        "calledIn": 0,
        "calledInReason": "-",
        "wbrgTicketNo": None,
        "gap": 0,
        "countryCode": "KE",
        # Images skipped as requested
        "lpImageFrontBase64": "",
        "lpImageBackBase64": "",
        "overviewImagesBase64": [],
        "axleWeights": [],
        "axle1Load": 0, "axle2Load": 0, "axle3Load": 0, "axle4Load": 0,
        "axle5Load": 0, "axle6Load": 0, "axle7Load": 0, "axle8Load": 0, "axle9Load": 0,
        "axle1LeftsideLoad": 0, "axle2LeftsideLoad": 0, "axle3LeftsideLoad": 0,
        "axle4LeftsideLoad": 0, "axle5LeftsideLoad": 0, "axle6LeftsideLoad": 0,
        "axle7LeftsideLoad": 0, "axle8LeftsideLoad": 0, "axle9LeftsideLoad": 0,
        "axle1RightsideLoad": 0, "axle2RightsideLoad": 0, "axle3RightsideLoad": 0,
        "axle4RightsideLoad": 0, "axle5RightsideLoad": 0, "axle6RightsideLoad": 0,
        "axle7RightsideLoad": 0, "axle8RightsideLoad": 0, "axle9RightsideLoad": 0,
        "axlLegalWeight1": 0, "axlLegalWeight2": 0, "axlLegalWeight3": 0,
        "axlLegalWeight4": 0, "axlLegalWeight5": 0, "axlLegalWeight6": 0,
        "axlLegalWeight7": 0, "axlLegalWeight8": 0, "axlLegalWeight9": 0,
    }
    return virtual_ticket


# ============================================================================
# CAMWIM POSTING
# ============================================================================

def post_to_camwim_service(virtual_ticket_request):
    """POST the VirtualTicketRequest to CAMWIM Service enhanced endpoint"""
    url = f"{CAMWIM_SERVICE_URL}{CAMWIM_ENHANCED_ENDPOINT}"
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=virtual_ticket_request, headers=headers, timeout=30)
        if response.status_code == 201:
            return True, response.json()
        else:
            logger.error(f"Failed to create virtual ticket. Status: {response.status_code} - {response.text}")
            return False, response.text
    except Exception as e:
        logger.error(f"Error posting to CAMWIM Service: {e}")
        return False, str(e)


def process_and_post_record(detection, record_id):
    """Map detection to VirtualTicket and post to CAMWIM Service"""
    virtual_ticket = map_detection_to_virtual_ticket(detection, record_id)
    for attempt in range(MAX_RETRIES):
        success, _ = post_to_camwim_service(virtual_ticket)
        if success:
            return True
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)
    return False


# ============================================================================
# PROGRESS PERSISTENCE (file + index - only read files with new data)
# ============================================================================

def _default_sent_state():
    return {
        "completed_files": [],
        "current_file": None,
        "current_index": -1,
        "next_ticket_id": 1,
    }


def load_sent_state():
    """Load sent state. Completed files are never re-read."""
    try:
        with open(SENT_STATE_FILE, 'r', encoding='utf-8') as f:
            s = json.load(f)
        return {
            "completed_files": s.get("completed_files", []),
            "current_file": s.get("current_file"),
            "current_index": s.get("current_index", -1),
            "next_ticket_id": s.get("next_ticket_id", 1),
        }
    except (FileNotFoundError, json.JSONDecodeError):
        return _default_sent_state()


def save_sent_state(state):
    """Persist sent state."""
    try:
        with open(SENT_STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=0)
    except Exception as e:
        logger.error(f"Failed to save sent state: {e}")


def iter_pending_detections(folder=DETECTIONS_FOLDER):
    """
    Yield only unsent detections. Reads ONLY files that may have new data:
    - Skips completed_files entirely (never reads them)
    - Reads current_file from current_index+1
    - Reads new files (after current) fully
    Yields (ticket_id, detection, filepath, basename, index, total_in_file).
    Call mark_sent() after each successful send.
    """
    state = load_sent_state()
    completed = set(state["completed_files"])
    current_file = state["current_file"]
    current_index = state["current_index"]
    next_ticket_id = state["next_ticket_id"]

    files = get_detection_json_files(folder)
    if not files:
        return

    files = sorted(files, key=lambda p: os.path.basename(p))

    if current_file:
        try:
            idx = next(i for i, p in enumerate(files) if os.path.basename(p) == current_file)
        except StopIteration:
            idx = 0
            current_file = None
            current_index = -1
    else:
        idx = 0

    for i in range(idx, len(files)):
        filepath = files[i]
        basename = os.path.basename(filepath)
        if basename in completed:
            continue

        detections = load_detections_from_file(filepath)
        start = (current_index + 1) if (basename == current_file) else 0
        total = len(detections)

        for j in range(start, total):
            yield next_ticket_id, detections[j], filepath, basename, j, total
            next_ticket_id += 1


def mark_sent(basename, index, total_in_file):
    """Mark detection as sent. Call after successful post."""
    state = load_sent_state()
    state["next_ticket_id"] = state.get("next_ticket_id", 1) + 1
    state["current_file"] = basename
    state["current_index"] = index
    if index == total_in_file - 1:
        state["completed_files"] = state.get("completed_files", []) + [basename]
        state["current_file"] = None
        state["current_index"] = -1
    save_sent_state(state)


def has_pending_detections(folder=DETECTIONS_FOLDER):
    """Check if there are unsent detections. Only does dir listing, no file reads."""
    state = load_sent_state()
    completed = set(state["completed_files"])
    files = get_detection_json_files(folder)
    for p in files:
        if os.path.basename(p) not in completed:
            return True
    if state["current_file"]:
        for p in files:
            if os.path.basename(p) == state["current_file"]:
                return True
    return False


# ============================================================================
# MAIN PROCESSING
# ============================================================================

def process_pending_detections(progress_tracker=None):
    """
    Send all unsent detections. Only reads files with new data (skips completed).
    Marks each sent record via mark_sent(). Returns (sent_count, success_count, failed_count).
    """
    records = list(iter_pending_detections())
    if not records:
        return 0, 0, 0

    first_id = records[0][0]
    last_id = records[-1][0]

    if progress_tracker:
        desc = f"Radar-ANPR detections (IDs {first_id}-{last_id})"
        if not progress_tracker.start_import(desc, first_id, last_id):
            return 0, 0, 0

    success_count = 0
    failed_count = 0

    try:
        for ticket_id, detection, filepath, basename, index, total in records:
            success = process_and_post_record(detection, ticket_id)
            if success:
                success_count += 1
                mark_sent(basename, index, total)
            else:
                failed_count += 1
                # Don't mark - will retry next poll

            if progress_tracker and (success_count + failed_count) % 10 == 0:
                progress_tracker.update_progress(ticket_id, success_count + failed_count, failed_count)

        if progress_tracker:
            progress_tracker.complete_import(success_count + failed_count, failed_count)

        return len(records), success_count, failed_count
    except Exception as e:
        logger.error(f"Error processing: {e}")
        if progress_tracker:
            progress_tracker.fail_import(str(e))
        raise


def run_watch_loop(progress_tracker=None, force_new=False):
    """
    Continuously poll for new detections, send unsent ones, mark as sent.
    Only reads files with new data (skips completed files). Runs until Ctrl+C.
    """
    if force_new and os.path.exists(SENT_STATE_FILE):
        os.remove(SENT_STATE_FILE)
        logger.info("Reset: cleared sent state (--force-new)")

    logger.info("Watch mode: polling every %d s. Only reads files with new data.", POLL_INTERVAL)

    while True:
        try:
            if not has_pending_detections():
                time.sleep(POLL_INTERVAL)
                continue

            sent, success, failed = process_pending_detections(progress_tracker=None)
            if sent > 0:
                logger.info("Sent: %d | Success: %d | Failed: %d", sent, success, failed)

        except KeyboardInterrupt:
            logger.info("Stopped by user (Ctrl+C)")
            break
        except Exception as e:
            logger.error("Watch loop error: %s", e)

        time.sleep(POLL_INTERVAL)


def process_all_detections(progress_tracker=None, limit=None):
    """
    One-shot: process all pending detections and exit.
    Only reads files with new data. If limit is set, process at most that many.
    """
    records = []
    for item in iter_pending_detections():
        records.append(item)
        if limit is not None and len(records) >= limit:
            break

    if not records:
        logger.info("No records to process")
        return True

    first_id = records[0][0]
    last_id = records[-1][0]
    total_to_process = len(records)

    if progress_tracker:
        desc = f"Radar-ANPR detections (IDs {first_id}-{last_id})"
        if not progress_tracker.start_import(desc, first_id, last_id):
            logger.error("Failed to start import operation")
            return False

    total_processed = 0
    total_success = 0
    total_failed = 0
    start_time = time.time()

    try:
        for ticket_id, detection, filepath, basename, index, total in records:
            success = process_and_post_record(detection, ticket_id)
            total_processed += 1
            if success:
                total_success += 1
                mark_sent(basename, index, total)
            else:
                total_failed += 1

            if progress_tracker and total_processed % 10 == 0:
                progress_tracker.update_progress(ticket_id, total_processed, total_failed)

            if total_processed % 10 == 0:
                pct = (total_processed / total_to_process) * 100
                remaining = total_to_process - total_processed
                elapsed = time.time() - start_time
                eta = (elapsed / total_processed * remaining) / 60 if total_processed > 0 else 0
                print(f"\rProgress: {total_processed}/{total_to_process} ({pct:.1f}%) - ETA: {eta:.1f}min", end="", flush=True)

        if progress_tracker:
            progress_tracker.complete_import(total_processed, total_failed)

        print()
        elapsed = time.time() - start_time
        logger.info("=" * 80)
        logger.info("PROCESSING COMPLETE (Radar-ANPR Detections JSON)")
        logger.info("=" * 80)
        logger.info(f"Total processed: {total_processed}")
        logger.info(f"Success: {total_success}")
        logger.info(f"Failed: {total_failed}")
        logger.info(f"Time: {elapsed / 60:.2f} minutes")
        logger.info("=" * 80)
        return True

    except Exception as e:
        logger.error(f"Fatal error: {e}")
        if progress_tracker:
            progress_tracker.fail_import(str(e))
        return False


def main():
    """Main entry point"""
    logger.info("=" * 80)
    logger.info("RADAR-ANPR DETECTIONS JSON -> CAMWIM VIRTUALTICKET MAPPER")
    logger.info("=" * 80)

    import sys
    args = sys.argv[1:]

    if '--help' in args or '-h' in args:
        print("Usage:")
        print("  python datamapper_detections_json.py              # Watch mode: poll for new detections, send & mark (default)")
        print("  python datamapper_detections_json.py --once        # One-shot: process all pending then exit")
        print("  python datamapper_detections_json.py --force-new  # Reset tracking, start from beginning")
        print("  python datamapper_detections_json.py --limit N    # (with --once) Process at most N records")
        print("  python datamapper_detections_json.py --test       # (with --once) Process 1 record only")
        print("  python datamapper_detections_json.py --help       # Show this help")
        return

    force_new = '--force-new' in args
    once = '--once' in args

    if once:
        progress_tracker = DataImportProgressTracker(CAMWIM_SERVICE_URL)
        limit = None
        if '--test' in args:
            limit = 1
            logger.info("Test mode: processing 1 record only")
        elif '--limit' in args:
            idx = args.index('--limit')
            if idx + 1 < len(args):
                try:
                    limit = int(args[idx + 1])
                    logger.info(f"Limit: processing at most {limit} records")
                except ValueError:
                    limit = None

        if force_new and os.path.exists(SENT_STATE_FILE):
            os.remove(SENT_STATE_FILE)

        success = process_all_detections(
            progress_tracker=progress_tracker,
            limit=limit
        )
        if success:
            logger.info("Import completed successfully")
        else:
            logger.error("Import failed")
    else:
        run_watch_loop(progress_tracker=None, force_new=force_new)


if __name__ == "__main__":
    main()
