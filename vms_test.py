#!/usr/bin/env python3
"""
Simple utility to test sending text to the VMS using the existing
send_plate_to_vms/clear_vms_display helpers from radaranprvms.py.
"""

import argparse
import time

import radaranprvms


def main():
    parser = argparse.ArgumentParser(description="Send a test plate/text to the VMS.")
    parser.add_argument("text", nargs="?", default="TEST-PLATE", help="Text/plate to display on the VMS.")
    parser.add_argument(
        "--stay",
        type=int,
        default=radaranprvms.VMS_STAY_TIME,
        help="Seconds to keep the text on screen before auto-clear (default: %(default)s).",
    )
    parser.add_argument(
        "--clear-only",
        action="store_true",
        help="Do not send text; just clear the VMS display.",
    )
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Do not wait for the auto-clear thread to finish.",
    )
    args = parser.parse_args()

    if args.clear_only:
        ok = radaranprvms.clear_vms_display()
        print("Cleared VMS display." if ok else "Failed to clear VMS display.")
        return

    # Override stay time for this run only.
    radaranprvms.VMS_STAY_TIME = args.stay

    print(f"Sending '{args.text}' to VMS at {radaranprvms.VMS_IP}:{radaranprvms.VMS_PORT} (stay {args.stay}s)...")
    ok = radaranprvms.send_plate_to_vms(args.text)
    if not ok:
        print("Send failed. Ensure sendcp5200 is installed and reachable.")
        return

    if args.no_wait:
        return

    # Wait a bit longer than stay time so the background clear thread can finish.
    time.sleep(args.stay + 1)


if __name__ == "__main__":
    main()

