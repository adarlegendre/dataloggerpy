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
CAMWIM_SERVICE_URL = "http://89.24.183.108:4445"
USE_REQUEST_WRAPPER = False  # Original datamapper sends body directly; set True if API returns "request field required"
CAMWIM_ENHANCED_ENDPOINT = "/api/wim/VirtualTicket/enhanced"
CAMWIM_PROGRESS_ENDPOINT = "/api/wim/DataImportProgress"

BATCH_SIZE = 50
MAX_RETRIES = 3
RETRY_DELAY = 2  # Seconds between retries (was 5 - too slow for realtime)
REQUEST_TIMEOUT = 10  # Seconds per HTTP request (was 30)
STATE_SAVE_INTERVAL = 5  # Save state every N records (avoids disk I/O per record)
SENT_STATE_FILE = 'datamapper_sent_state.json'  # Tracks (file, index) - only reads files with new data
SYNC_FLAG_FILE = os.path.join(DETECTIONS_FOLDER, '.sync_needed')  # radaranprvms writes when file changes
POLL_INTERVAL = 0.5  # Seconds between checks (was 1 - faster for realtime)


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
        # DD_MM_YYYY.json = 15 chars (e.g. 23_02_2026.json)
        if f.endswith('.json') and len(f) == 15 and f[2] == '_' and f[5] == '_':
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
    if isinstance(timestamp, str) and timestamp.strip():
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            date_time_local = dt.strftime('%Y-%m-%dT%H:%M:%S')
        except (ValueError, TypeError):
            date_time_local = timestamp
    elif timestamp:
        date_time_local = str(timestamp)
    else:
        date_time_local = "UNKNOWN"

    # Handle null/empty - use UNKNOWN per working datamapper pattern
    plate = detection.get('plate_number')
    if plate is None or (isinstance(plate, str) and not plate.strip()):
        plate = "UNKNOWN"
    else:
        plate = str(plate).strip()

    direction = detection.get('direction')
    if direction is None or (isinstance(direction, str) and not direction.strip()):
        direction = "UNKNOWN"
    else:
        direction = str(direction).strip()

    speed = detection.get('speed') or 0

    # Match original datamapper: camelCase, sent as root body (no request wrapper)
    virtual_ticket = {
        "ticketId": record_id,
        "cid": record_id,
        "dateTimeLocal": date_time_local,
        "wim": direction,
        "vehicleClass": 1,
        "velocity": int(speed) if speed is not None else 0,
        "length": 0,
        "licensePlate": plate,
        "anprAssist": None,
        "licensePlateBack": "UNKNOWN",
        "totalWeight": 0,
        "axlesCount": 0,
        "axleConf": "2*SS",
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

def post_to_camwim_service(virtual_ticket_request, session=None):
    """POST the VirtualTicketRequest to CAMWIM Service. Use session for connection reuse."""
    url = f"{CAMWIM_SERVICE_URL}{CAMWIM_ENHANCED_ENDPOINT}"
    headers = {'Content-Type': 'application/json'}
    payload = {"request": virtual_ticket_request} if USE_REQUEST_WRAPPER else virtual_ticket_request
    http = session or requests
    try:
        response = http.post(url, json=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        if response.status_code == 201:
            return True, response.json()
        else:
            logger.error(f"Failed to create virtual ticket. Status: {response.status_code} - {response.text}")
            return False, response.text
    except Exception as e:
        logger.error(f"Error posting to CAMWIM Service: {e}")
        return False, str(e)


def process_and_post_record(detection, record_id, session=None):
    """Map detection to VirtualTicket and post to CAMWIM Service. Returns (success, virtual_ticket for logging)."""
    virtual_ticket = map_detection_to_virtual_ticket(detection, record_id)
    for attempt in range(MAX_RETRIES):
        success, resp = post_to_camwim_service(virtual_ticket, session=session)
        if success:
            return True, virtual_ticket
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)
    return False, virtual_ticket


# ============================================================================
# PROGRESS PERSISTENCE (file + index - only read files with new data)
# ============================================================================

def _default_sent_state():
    return {
        "completed_files": [],
        "completed_file_last_index": {},  # {basename: last_index} for re-processing when flag says file changed
        "current_file": None,
        "current_index": -1,
        "active_file_last_index": -1,  # When on backlog: last sent index for today's file
        "next_ticket_id": 1,
    }


def load_sent_state():
    """Load sent state. completed_file_last_index allows re-reading completed files when sync flag says they changed."""
    try:
        with open(SENT_STATE_FILE, 'r', encoding='utf-8') as f:
            s = json.load(f)
        completed = s.get("completed_files", [])
        cfli = s.get("completed_file_last_index", {})
        if isinstance(completed, list) and not cfli:
            cfli = {f: -1 for f in completed}
        return {
            "completed_files": completed,
            "completed_file_last_index": cfli,
            "current_file": s.get("current_file"),
            "current_index": s.get("current_index", -1),
            "active_file_last_index": s.get("active_file_last_index", -1),
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


def _basename_eq(a, b):
    """Case-insensitive basename comparison (Windows can have .json vs .JSON)."""
    return (a or "").lower() == (b or "").lower()


def _find_in_list(files, target_basename):
    """Find file path whose basename matches target (case-insensitive)."""
    t = (target_basename or "").lower()
    for p in files:
        if os.path.basename(p).lower() == t:
            return p
    return None


def mark_file_complete(basename, filepath):
    """Mark file as complete without sending (empty file or already sent all). Unsticks the mapper.
    Skips today's file - it can keep growing."""
    if _basename_eq(basename, get_active_file_basename()):
        return  # Today's file: don't mark complete, it may get new records
    detections = load_detections_from_file(filepath)
    total = len(detections)
    last_index = total - 1 if total > 0 else -1
    state = load_sent_state()
    state.setdefault("completed_file_last_index", {})
    if basename not in state.get("completed_files", []):
        state["completed_files"] = state.get("completed_files", []) + [basename]
    state["completed_file_last_index"][basename] = last_index
    if _basename_eq(state.get("current_file"), basename):
        state["current_file"] = None
        state["current_index"] = -1
    save_sent_state(state)
    logger.info("Marked %s complete (0 records to send, total=%d)", basename, total)


def iter_pending_detections(folder=DETECTIONS_FOLDER, prioritize_active=True, force_process_file=None):
    """
    Yield only unsent detections. Efficient tracking:
    - completed_files: past files fully synced; re-read when sync flag says they changed
    - completed_file_last_index: last sent index per completed file (for re-processing)
    - current_file + current_index: partial progress (resume after crash)
    - active_file_last_index: when on backlog, last sent index for today's file
    - force_process_file: when sync flag says this file changed, process it first (any file)
    Yields (ticket_id, detection, filepath, basename, index, total_in_file).
    Call mark_sent() after each successful send.
    """
    state = load_sent_state()
    completed = set(state["completed_files"])
    cfli = state.get("completed_file_last_index", {})
    current_file = state["current_file"]
    current_index = state["current_index"]
    active_file_last_index = state.get("active_file_last_index", -1)
    next_ticket_id = state["next_ticket_id"]

    files = get_detection_json_files(folder)
    if not files:
        return

    files = sorted(files, key=lambda p: os.path.basename(p))
    active_basename = get_active_file_basename()
    completed_lower = {b.lower() for b in completed}

    def process_file(filepath, basename, start_override=None):
        nonlocal next_ticket_id
        detections = load_detections_from_file(filepath)
        if start_override is not None:
            start = start_override
        else:
            start = (current_index + 1) if _basename_eq(basename, current_file) else 0
        total = len(detections)
        for j in range(start, total):
            yield next_ticket_id, detections[j], filepath, basename, j, total
            next_ticket_id += 1

    def start_for_file(basename):
        if _basename_eq(basename, current_file):
            return current_index + 1
        if basename.lower() in completed_lower:
            cfli_key = next((k for k in cfli if k.lower() == basename.lower()), basename)
            return cfli.get(cfli_key, -1) + 1
        if _basename_eq(basename, active_basename):
            return active_file_last_index + 1
        return 0

    def is_completed(basename):
        return basename.lower() in completed_lower

    # 1. When sync flag says a specific file changed: process that file first (today, past, or completed)
    if force_process_file:
        target_path = _find_in_list(files, force_process_file)
        if target_path:
            start = start_for_file(force_process_file)
            gen = process_file(target_path, os.path.basename(target_path), start_override=start)
            first = next(gen, None)
            if first is None:
                mark_file_complete(os.path.basename(target_path), target_path)
            else:
                yield first
                for item in gen:
                    yield item
            return

    # 2. When prioritize_active and we're on today's file: process active first
    if prioritize_active and _basename_eq(active_basename, current_file):
        active_path = _find_in_list(files, active_basename)
        if active_path:
            start = start_for_file(active_basename)
            for item in process_file(active_path, active_basename, start_override=start):
                yield item
            return

    # 3. Backlog: process in chronological order (oldest first)
    if current_file:
        idx = next((i for i, p in enumerate(files) if _basename_eq(os.path.basename(p), current_file)), None)
        if idx is None:
            idx = 0
            current_file = None
            current_index = -1
    else:
        idx = 0

    for i in range(idx, len(files)):
        filepath = files[i]
        basename = os.path.basename(filepath)
        if is_completed(basename):
            continue
        if prioritize_active and _basename_eq(basename, active_basename):
            continue
        gen = process_file(filepath, basename, start_override=None)
        first = next(gen, None)
        if first is None:
            mark_file_complete(basename, filepath)
            continue
        yield first
        for item in gen:
            yield item


def mark_sent(basename, index, total_in_file):
    """Mark detection as sent. Call after successful post."""
    state = load_sent_state()
    state.setdefault("completed_file_last_index", {})
    state["next_ticket_id"] = state.get("next_ticket_id", 1) + 1
    state["current_file"] = basename
    state["current_index"] = index
    if basename == get_active_file_basename():
        state["active_file_last_index"] = index
    if basename in state.get("completed_files", []):
        state["completed_file_last_index"][basename] = index
    # Only mark file complete if we've sent the last record AND it's not today's file.
    # Today's file can keep growing (radaranprvms appends); we must keep checking it.
    if index == total_in_file - 1:
        if basename != get_active_file_basename():
            state["completed_file_last_index"][basename] = index
            if basename not in state.get("completed_files", []):
                state["completed_files"] = state.get("completed_files", []) + [basename]
            state["current_file"] = None
            state["current_index"] = -1
        # else: keep current_file/current_index so next poll re-reads and gets new records
    save_sent_state(state)


def has_pending_detections(folder=DETECTIONS_FOLDER):
    """Check if there are unsent detections. Includes sync flag: completed file changed = pending."""
    state = load_sent_state()
    completed = set(state["completed_files"])
    completed_lower = {b.lower() for b in completed}
    files = get_detection_json_files(folder)
    for p in files:
        if os.path.basename(p).lower() not in completed_lower:
            return True
    if state["current_file"]:
        for p in files:
            if _basename_eq(os.path.basename(p), state["current_file"]):
                return True
    flag = read_sync_flag()
    if flag and flag.get("file") and flag.get("file").lower() in completed_lower:
        return True
    return False


def get_active_file_basename():
    """Today's file - the one radaranprvms is actively appending to."""
    return datetime.now().strftime('%d_%m_%Y.json')


def read_sync_flag():
    """Read .sync_needed flag written by radaranprvms when it writes detections. Returns {"file": basename, "ts": iso} or None."""
    try:
        if os.path.exists(SYNC_FLAG_FILE):
            with open(SYNC_FLAG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, dict) and data.get("file") else None
    except Exception:
        pass
    return None


def is_on_active_file():
    """True if we're currently processing the active (today's) file."""
    state = load_sent_state()
    return _basename_eq(state.get("current_file"), get_active_file_basename())


def get_sync_status(folder=DETECTIONS_FOLDER):
    """
    Return sync status: (total_files, completed_count, backlog_count, current_file, on_active).
    Efficient: only dir listing + state read, no file content reads.
    """
    state = load_sent_state()
    completed = set(state["completed_files"])
    completed_lower = {b.lower() for b in completed}
    files = get_detection_json_files(folder)
    total = len(files)
    completed_count = sum(1 for p in files if os.path.basename(p).lower() in completed_lower)
    backlog_count = total - completed_count
    if state["current_file"] and state["current_file"] not in completed:
        backlog_count = max(1, backlog_count)
    return {
        "total_files": total,
        "completed_count": completed_count,
        "backlog_count": backlog_count,
        "current_file": state.get("current_file"),
        "on_active_file": is_on_active_file(),
    }


# ============================================================================
# PREVIEW (no POST)
# ============================================================================

def preview_pending(count=1):
    """Show payload for pending records without posting. Returns number shown."""
    records = list(iter_pending_detections())
    if not records:
        logger.info("No pending records to preview")
        return 0
    for i, (ticket_id, detection, filepath, basename, idx, total) in enumerate(records[:count]):
        payload = map_detection_to_virtual_ticket(detection, ticket_id)
        print("\n" + "=" * 60)
        print(f"PREVIEW record {i + 1}/{min(count, len(records))} (no POST)")
        print("=" * 60)
        print(f"Source: {basename} index {idx}")
        print(f"ticketId: {payload.get('ticketId')}")
        print(f"licensePlate: {payload.get('licensePlate')}")
        print(f"wim: {payload.get('wim')}")
        print(f"dateTimeLocal: {payload.get('dateTimeLocal')}")
        print(f"velocity: {payload.get('velocity')}")
        print("=" * 60)
    return min(count, len(records))


# ============================================================================
# MAIN PROCESSING
# ============================================================================

def _apply_mark_sent_to_state(state, basename, index, total_in_file):
    """Apply mark_sent updates to state dict (no disk I/O)."""
    state.setdefault("completed_file_last_index", {})
    state["next_ticket_id"] = state.get("next_ticket_id", 1) + 1
    state["current_file"] = basename
    state["current_index"] = index
    if basename == get_active_file_basename():
        state["active_file_last_index"] = index
    if basename in state.get("completed_files", []):
        state["completed_file_last_index"][basename] = index
    if index == total_in_file - 1 and basename != get_active_file_basename():
        state["completed_file_last_index"][basename] = index
        if basename not in state.get("completed_files", []):
            state["completed_files"] = state.get("completed_files", []) + [basename]
        state["current_file"] = None
        state["current_index"] = -1


def process_pending_detections(progress_tracker=None, force_process_file=None):
    """
    Send all unsent detections. Streams records (no bulk load). Batch-saves state every N records.
    Returns (sent_count, success_count, failed_count).
    force_process_file: when sync flag indicates this file changed, process it first (any file).
    """
    session = requests.Session()
    state = load_sent_state()
    first_id = None
    success_count = 0
    failed_count = 0

    try:
        for ticket_id, detection, filepath, basename, index, total in iter_pending_detections(force_process_file=force_process_file):
            if first_id is None:
                first_id = ticket_id
                if progress_tracker:
                    if not progress_tracker.start_import(f"Radar-ANPR detections from {basename}", ticket_id, ticket_id):
                        return 0, 0, 0

            success, vt = process_and_post_record(detection, ticket_id, session=session)
            if success:
                success_count += 1
                _apply_mark_sent_to_state(state, basename, index, total)
                # Realtime: show each record sent immediately (flush for unbuffered output)
                msg = "SENT #%s | %s | %s | %s km/h | %s" % (
                    vt.get("ticketId"), vt.get("licensePlate"), vt.get("wim"),
                    vt.get("velocity"), vt.get("dateTimeLocal"))
                logger.info(msg)
                print(msg, flush=True)
                if success_count % STATE_SAVE_INTERVAL == 0:
                    save_sent_state(state)
            else:
                failed_count += 1

            if progress_tracker and (success_count + failed_count) % 10 == 0:
                progress_tracker.update_progress(ticket_id, success_count + failed_count, failed_count)

        save_sent_state(state)
        if progress_tracker and first_id is not None:
            progress_tracker.complete_import(success_count + failed_count, failed_count)

        return success_count + failed_count, success_count, failed_count
    except Exception as e:
        save_sent_state(state)
        logger.error(f"Error processing: {e}")
        if progress_tracker:
            progress_tracker.fail_import(str(e))
        raise


def run_watch_loop(progress_tracker=None, force_new=False):
    """
    Continuously poll for new detections, send unsent ones, mark as sent.
    - Completed files: never re-read
    - Current file: sends from last_index+1 (only new records)
    - Active file (today's): when reached, sends per new records added; keeps checking
      until caught up so new detections are sent promptly as radaranprvms appends them.
    """
    if force_new and os.path.exists(SENT_STATE_FILE):
        os.remove(SENT_STATE_FILE)
        logger.info("Reset: cleared sent state (--force-new)")

    logger.info("Watch mode: polling every %.1f s. Realtime send logging enabled.", POLL_INTERVAL)
    ACTIVE_FILE_CATCHUP_INTERVAL = 0.1  # Seconds between re-checks when on active file (was 0.2)
    ACTIVE_FILE_MAX_ITERATIONS = 100     # Max catchup iterations per poll cycle

    while True:
        try:
            # Sync flag: radaranprvms writes .sync_needed when ANY file is written
            sync_flag = read_sync_flag()
            force_file = sync_flag.get("file") if sync_flag else None

            if not has_pending_detections():
                time.sleep(POLL_INTERVAL)
                continue

            status = get_sync_status()
            if status["backlog_count"] > 0 or force_file:
                logger.info("Sync: %d/%d files done, %d backlog | current: %s%s",
                    status["completed_count"], status["total_files"], status["backlog_count"],
                    status["current_file"] or "none",
                    f" | flag: {force_file}" if force_file else "")

            # When on backlog (stuck on a past file): process backlog first so we don't starve.
            # Otherwise the sync flag (today's file) would always win and we'd never finish yesterday's file.
            if not status["on_active_file"] and status.get("current_file"):
                sent, success, failed = process_pending_detections(progress_tracker=None)
                if sent > 0:
                    logger.info("Sent: %d | Success: %d | Failed: %d", sent, success, failed)
            # When sync flag says a file changed or we're on today's file: process that file (with prioritization)
            elif force_file or is_on_active_file():
                total_sent = 0
                for _ in range(ACTIVE_FILE_MAX_ITERATIONS):
                    pf = force_file if force_file else (get_active_file_basename() if is_on_active_file() else None)
                    sent, success, failed = process_pending_detections(progress_tracker=None, force_process_file=pf)
                    if sent == 0:
                        break
                    total_sent += sent
                    logger.info("Active file %s: sent %d | Success: %d | Failed: %d", get_active_file_basename(), sent, success, failed)
                    time.sleep(ACTIVE_FILE_CATCHUP_INTERVAL)
                if total_sent > 0:
                    logger.info("Caught up on active file. Total sent this cycle: %d", total_sent)
            else:
                sent, success, failed = process_pending_detections(progress_tracker=None)
                if sent > 0:
                    logger.info("Sent: %d | Success: %d | Failed: %d", sent, success, failed)

        except KeyboardInterrupt:
            logger.info("Stopped by user (Ctrl+C)")
            break
        except Exception as e:
            logger.error("Watch loop error: %s", e)

        time.sleep(POLL_INTERVAL)


def _log_no_records_reason():
    """Log why no records were found to help diagnose."""
    folder = DETECTIONS_FOLDER
    if not os.path.exists(folder):
        logger.info("No records to process: folder '%s' does not exist. Run radaranprvms.py first to create detections.", folder)
        return
    files = get_detection_json_files(folder)
    if not files:
        logger.info("No records to process: folder '%s' is empty or has no DD_MM_YYYY.json files. Run radaranprvms.py to generate detections.", folder)
        return
    state = load_sent_state()
    total_detections = sum(len(load_detections_from_file(p)) for p in files)
    if total_detections == 0:
        logger.info("No records to process: %d JSON file(s) found but all are empty.", len(files))
        return
    if state["completed_files"] and len(state["completed_files"]) >= len(files):
        logger.info("No records to process: all %d detection(s) across %d file(s) already sent.", total_detections, len(files))
        return
    logger.info("No records to process: %d file(s), %d total detection(s). Check datamapper_sent_state.json if resuming.", len(files), total_detections)


def process_all_detections(progress_tracker=None, limit=None):
    """
    One-shot: process all pending detections and exit.
    Streams records, batch-saves state, realtime logging.
    """
    session = requests.Session()
    state = load_sent_state()
    first_id = None
    total_processed = 0
    total_success = 0
    total_failed = 0
    start_time = time.time()

    try:
        for ticket_id, detection, filepath, basename, index, total in iter_pending_detections():
            if first_id is None:
                first_id = ticket_id
                if progress_tracker:
                    if not progress_tracker.start_import(f"Radar-ANPR detections from {basename}", ticket_id, ticket_id):
                        return False

            success, vt = process_and_post_record(detection, ticket_id, session=session)
            total_processed += 1
            if success:
                total_success += 1
                _apply_mark_sent_to_state(state, basename, index, total)
                msg = "SENT #%s | %s | %s | %s km/h | %s" % (
                    vt.get("ticketId"), vt.get("licensePlate"), vt.get("wim"),
                    vt.get("velocity"), vt.get("dateTimeLocal"))
                logger.info(msg)
                print(msg, flush=True)
                if total_success % STATE_SAVE_INTERVAL == 0:
                    save_sent_state(state)
            else:
                total_failed += 1

            if progress_tracker and total_processed % 10 == 0:
                progress_tracker.update_progress(ticket_id, total_processed, total_failed)

            if limit is not None and total_processed >= limit:
                break

        save_sent_state(state)

        if total_processed == 0:
            _log_no_records_reason()
            return True

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
        print("  python datamapper_detections_json.py --test        # (with --once) Process 1 record only - verify API")
        print("  python datamapper_detections_json.py --limit N    # (with --once) Process at most N records")
        print("  python datamapper_detections_json.py --preview [N] # Show payload for 1 (or N) pending records, no POST")
        print("  python datamapper_detections_json.py --force-new  # Reset tracking, start from beginning")
        print("  python datamapper_detections_json.py --help        # Show this help")
        return

    force_new = '--force-new' in args
    once = '--once' in args

    # --preview: show payload without posting
    if '--preview' in args:
        preview_count = 1
        idx = args.index('--preview')
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            preview_count = int(args[idx + 1])
        if force_new and os.path.exists(SENT_STATE_FILE):
            os.remove(SENT_STATE_FILE)
        preview_pending(preview_count)
        return

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
