#!/usr/bin/env python3
"""
Dev Box Setup — Stage 2: Login (authenticate to services)

Handles GitHub CLI authentication so gopass, chezmoi, and other tools
that pull from private repos can operate.

Usage:
  python3 stage_2_login.py                  Run login steps interactively
  python3 stage_2_login.py --list           Show login steps
  python3 stage_2_login.py --dry-run        Preview without executing
  python3 stage_2_login.py --unattended     Check status only, skip interactive login
"""

import argparse
import subprocess
import sys


STEPS = {
    "gh-auth": {
        "name": "gh-auth",
        "description": "GitHub CLI authentication",
        "check": "gh auth status",
        "command": "gh auth login --hostname github.com --git-protocol ssh --web",
        "interactive": True,
    },
}


def is_done(step):
    check = step.get("check", "")
    if not check:
        return False
    try:
        subprocess.run(check, shell=True, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def run_cmd(cmd):
    print(f"  → {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, executable="/bin/bash")
        return result.returncode == 0
    except KeyboardInterrupt:
        print("\n  ⏎ Skipped (Ctrl+C)")
        return False


def run_login(unattended=False, dry_run=False):
    for key, step in STEPS.items():
        name = step["name"]
        print(f"\n─── {name} ────────────────────")

        if is_done(step):
            print(f"  ✓ Already authenticated — skipping")
            continue

        if step.get("interactive") and unattended:
            print(f"  ⚠  Interactive — skipping in unattended mode")
            continue

        cmd = step["command"]

        if dry_run:
            print(f"  [dry-run] → {cmd}")
            continue

        if not run_cmd(cmd):
            print(f"  ✗ Failed: {cmd}")
            return 1

        print(f"  ✓ Done")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Dev Box Setup — Stage 2: Login"
    )
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--unattended", action="store_true")
    parser.add_argument("--select", type=str, help="(ignored in stage 2)")
    parser.add_argument("--packages-dir", type=str, help="(ignored in stage 2)")
    args = parser.parse_args()

    if args.list:
        for key, step in STEPS.items():
            ok = "✓" if is_done(step) else " "
            tag = "⚡" if step.get("interactive") else "  "
            print(f"  {tag}[{ok}] {step['name']:28s}  {step.get('description', '')}")
        sys.exit(0)

    sys.exit(run_login(unattended=args.unattended, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
