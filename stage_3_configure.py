#!/usr/bin/env python3
"""
Dev Box Setup — Stage 3: Configure (system settings, shell, dotfiles)

Handles system-level configuration that stage 1 (install) and stage 2 (login)
don't cover: switching default shell to zsh, applying chezmoi dotfiles.

Usage:
  python3 stage_3_configure.py                  Run config steps interactively
  python3 stage_3_configure.py --list            Show config steps
  python3 stage_3_configure.py --dry-run         Preview without executing
  python3 stage_3_configure.py --unattended      Check status, skip interactive steps
"""

import argparse
import subprocess
import sys
from pathlib import Path

CHEZMOI = str(Path.home() / "dev-setup/bin/chezmoi")

STEPS = {
    "chsh-zsh": {
        "name": "chsh-zsh",
        "description": "Set default shell to zsh",
        "check": 'test "$(getent passwd $USER | cut -d: -f7)" = "$(which zsh)"',
        "command": "chsh -s $(which zsh)",
        "interactive": True,
    },
    "chezmoi-apply": {
        "name": "chezmoi-apply",
        "description": "Apply chezmoi dotfiles to $HOME",
        "check": f"{CHEZMOI} status",
        "command": f"{CHEZMOI} apply -v",
        "interactive": False,
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


def run_configure(unattended=False, dry_run=False):
    failed = 0

    for key, step in STEPS.items():
        name = step["name"]
        print(f"\n─── {name} ─────────────────────")

        if is_done(step):
            print(f"  ✓ Already configured — skipping")
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
            failed += 1
            continue

        print(f"  ✓ Done")

    return failed


def main():
    parser = argparse.ArgumentParser(
        description="Dev Box Setup — Stage 3: Configure"
    )
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--unattended", action="store_true")
    parser.add_argument("--select", type=str, help="(ignored in stage 3)")
    parser.add_argument("--packages-dir", type=str, help="(ignored in stage 3)")
    args = parser.parse_args()

    if args.list:
        for key, step in STEPS.items():
            ok = "✓" if is_done(step) else " "
            tag = "⚡" if step.get("interactive") else "  "
            print(f"  {tag}[{ok}] {step['name']:20s}  {step.get('description', '')}")
        sys.exit(0)

    failed = run_configure(unattended=args.unattended, dry_run=args.dry_run)
    if failed:
        print(f"\n  {failed} step(s) failed")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
