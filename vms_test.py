#!/usr/bin/env python3
"""
Standalone VMS test utility.

Sends text to the CP5200 display via sendcp5200 and (optionally) clears it
after the configured stay time. No radar, camera, or other dependencies.
"""

import argparse
import os
import subprocess
import time

# Default VMS configuration
DEFAULT_VMS_IP = "192.168.1.222"
DEFAULT_VMS_PORT = 5200
DEFAULT_VMS_WINDOW = 0
DEFAULT_VMS_COLOR = 3
DEFAULT_VMS_FONT_SIZE = 18
DEFAULT_VMS_SPEED = 5
DEFAULT_VMS_EFFECT = 1
DEFAULT_VMS_STAY_TIME = 3
DEFAULT_VMS_ALIGNMENT = 1

# Common lookup paths for the sendcp5200 executable
SENDCP5200_PATHS = [
    "./sendcp5200/dist/Debug/GNU-Linux/sendcp5200",
    "./sendcp5200/dist/Release/GNU-Linux/sendcp5200",
    "/etc/1prog/sendcp5200k",
    "sendcp5200",
    "/usr/local/bin/sendcp5200",
    "/usr/bin/sendcp5200",
]


def find_sendcp5200(executable_override: str | None = None) -> str | None:
    """Locate the sendcp5200 executable."""
    if executable_override:
        return executable_override if os.path.exists(executable_override) else None

    for path in SENDCP5200_PATHS:
        if os.path.exists(path) and os.access(path, os.X_OK):
            return path

    for cmd in (["which", "sendcp5200"], ["where", "sendcp5200"]):
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                found = result.stdout.strip().splitlines()
                if found:
                    return found[0]
        except Exception:
            pass

    return None


def send_to_vms(
    text: str,
    executable: str,
    *,
    ip: str,
    port: int,
    window: int,
    color: int,
    font_size: int,
    speed: int,
    effect: int,
    stay_time: int,
    alignment: int,
) -> bool:
    """Send text to VMS using sendcp5200."""
    cmd = [
        executable,
        "0",
        ip,
        str(port),
        "2",
        str(window),
        text,
        str(color),
        str(font_size),
        str(speed),
        str(effect),
        str(stay_time),
        str(alignment),
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return True
        print(f"sendcp5200 exit code {result.returncode}: {result.stderr.strip()}")
        return False
    except Exception as exc:
        print(f"Error running sendcp5200: {exc}")
        return False


def clear_vms(executable: str, *, ip: str, port: int, window: int, font_size: int, speed: int, effect: int, alignment: int) -> bool:
    """Clear the VMS display by sending an empty string."""
    return send_to_vms(
        "",
        executable,
        ip=ip,
        port=port,
        window=window,
        color=DEFAULT_VMS_COLOR,
        font_size=font_size,
        speed=speed,
        effect=effect,
        stay_time=10,
        alignment=alignment,
    )


def main():
    parser = argparse.ArgumentParser(description="Send a test message to the VMS (no radar/camera required).")
    parser.add_argument("text", nargs="?", default="TEST-PLATE", help="Text to display.")
    parser.add_argument("--ip", default=DEFAULT_VMS_IP, help="VMS IP address.")
    parser.add_argument("--port", type=int, default=DEFAULT_VMS_PORT, help="VMS port.")
    parser.add_argument("--window", type=int, default=DEFAULT_VMS_WINDOW, help="Display window/index.")
    parser.add_argument("--color", type=int, default=DEFAULT_VMS_COLOR, help="Font color index.")
    parser.add_argument("--font-size", type=int, default=DEFAULT_VMS_FONT_SIZE, help="Font size.")
    parser.add_argument("--speed", type=int, default=DEFAULT_VMS_SPEED, help="Scroll speed.")
    parser.add_argument("--effect", type=int, default=DEFAULT_VMS_EFFECT, help="Display effect.")
    parser.add_argument("--stay", type=int, default=DEFAULT_VMS_STAY_TIME, help="Seconds to keep text on screen.")
    parser.add_argument("--alignment", type=int, default=DEFAULT_VMS_ALIGNMENT, help="Alignment code.")
    parser.add_argument("--executable", help="Path to sendcp5200 (optional).")
    parser.add_argument("--clear-only", action="store_true", help="Only clear the display; do not show text.")
    parser.add_argument("--no-auto-clear", action="store_true", help="Skip clearing after stay time.")
    args = parser.parse_args()

    executable = find_sendcp5200(args.executable)
    if not executable:
        print("sendcp5200 not found. Provide --executable or install sendcp5200.")
        return

    if args.clear_only:
        ok = clear_vms(
            executable,
            ip=args.ip,
            port=args.port,
            window=args.window,
            font_size=args.font_size,
            speed=args.speed,
            effect=args.effect,
            alignment=args.alignment,
        )
        print("Cleared VMS display." if ok else "Failed to clear VMS display.")
        return

    print(f"Sending '{args.text}' to VMS at {args.ip}:{args.port} (stay {args.stay}s)...")
    ok = send_to_vms(
        args.text,
        executable,
        ip=args.ip,
        port=args.port,
        window=args.window,
        color=args.color,
        font_size=args.font_size,
        speed=args.speed,
        effect=args.effect,
        stay_time=args.stay,
        alignment=args.alignment,
    )
    if not ok:
        print("Send failed. Ensure sendcp5200 is installed and reachable.")
        return

    if args.no_auto_clear:
        return

    time.sleep(args.stay)
    cleared = clear_vms(
        executable,
        ip=args.ip,
        port=args.port,
        window=args.window,
        font_size=args.font_size,
        speed=args.speed,
        effect=args.effect,
        alignment=args.alignment,
    )
    print("Auto-cleared display." if cleared else "Failed to auto-clear display.")


if __name__ == "__main__":
    main()
