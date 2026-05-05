#!/usr/bin/env python3
"""
Dev Box Setup — orchestrator for the multi-stage pipeline.

Stages:
  1. Install  — stage_1_install.py    (package installation)
  2. Login    — stage_2_login.py       (authenticate to services)
  3. Configure — stage_3_configure.py  (shell, dotfiles, system settings)

Usage:
  python3 setup.py                     TUI — pick a stage, then select packages
  python3 setup.py --all                Run all stages, skip interactive
  python3 setup.py --unattended         Same as --all, exit non-zero on failure
  python3 setup.py --select git,gh      Install specific packages by name
  python3 setup.py --list               List all packages grouped by source
  python3 setup.py --dry-run            Preview commands without executing
  python3 setup.py --stage 2            Run a single stage (TUI)
  python3 setup.py --from-stage 3       Run from stage N onward
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("GOBIN", os.path.expanduser("~/.local/bin"))
os.environ.setdefault("GOPATH", os.path.expanduser("~/.local/share/go"))
# Prepend ~/.local/bin (new go-install target); keep legacy ~/go/bin as fallback
home = os.path.expanduser("~")
paths = [f"{home}/.local/bin", f"{home}/go/bin"] + os.environ.get("PATH", "").split(":")
# dedupe preserving order
seen = set()
new_path = ":".join(p for p in paths if p and not (p in seen or seen.add(p)))
os.environ["PATH"] = new_path

SCRIPT_DIR = Path(__file__).resolve().parent

STAGE_SCRIPTS = {
    1: SCRIPT_DIR / "stage_1_install.py",
    2: SCRIPT_DIR / "stage_2_login.py",
    3: SCRIPT_DIR / "stage_3_configure.py",
}


def run_stage(stage_num, args):
    script = STAGE_SCRIPTS.get(stage_num)
    if script is None:
        print(f"✗ Unknown stage: {stage_num}", file=sys.stderr)
        return 1

    if not script.is_file():
        print(f"✗ Stage {stage_num} script not found: {script}", file=sys.stderr)
        return 1

    cmd = [sys.executable, str(script)] + args
    result = subprocess.run(cmd)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Dev Box Setup — multi-stage pipeline"
    )
    parser.add_argument("--all", action="store_true", help="Run all stages")
    parser.add_argument("--unattended", action="store_true", help="Run all stages, exit non-zero on failure")
    parser.add_argument("--select", type=str, help="Comma-separated package names")
    parser.add_argument("--list", action="store_true", help="List all packages grouped by source")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--stage", type=int, help="Run a single stage (e.g. --stage 2)")
    parser.add_argument("--from-stage", type=int, help="Run from stage N onward")
    parser.add_argument("--packages-dir", type=str, help="Directory containing package .yaml files")
    args = parser.parse_args()

    extra = []
    if args.select:
        extra.extend(["--select", args.select])
    if args.list:
        extra.append("--list")
    if args.dry_run:
        extra.append("--dry-run")
    if args.unattended:
        extra.append("--unattended")
    if args.packages_dir:
        extra.extend(["--packages-dir", args.packages_dir])

    # ── --stage ─────────────────────────────────────────────────────────
    if args.stage:
        stage = args.stage
        if args.list:
            # --list is per-stage passthrough; just run that stage with --list
            sys.exit(run_stage(stage, ["--list"]))
        sys.exit(run_stage(stage, extra))

    # ── --from-stage ─────────────────────────────────────────────────────
    if args.from_stage:
        start = args.from_stage
        for stage_num in sorted(STAGE_SCRIPTS):
            if stage_num < start:
                continue
            print(f"\n═══ Stage {stage_num} ═══")
            rc = run_stage(stage_num, extra)
            if rc != 0:
                sys.exit(rc)
        sys.exit(0)

    # ── --all / --unattended ─────────────────────────────────────────────
    if args.all or args.unattended:
        for stage_num in sorted(STAGE_SCRIPTS):
            print(f"\n═══ Stage {stage_num} ═══")
            rc = run_stage(stage_num, extra)
            if rc != 0:
                sys.exit(rc)
        sys.exit(0)

    # ── --select / --list (no stage specified, default to stage 1) ───────
    if args.select or args.list:
        sys.exit(run_stage(1, extra))

    # ── default TUI ──────────────────────────────────────────────────────
    try:
        import questionary
    except ImportError:
        print("✗ questionary is required for TUI mode.", file=sys.stderr)
        print("   Install it with: pip install questionary", file=sys.stderr)
        sys.exit(1)

    stage_choices = []
    for num in sorted(STAGE_SCRIPTS):
        label = f"Stage {num}"
        stage_choices.append(questionary.Choice(title=label, value=num))

    stage = questionary.select(
        "Pick a stage to run:",
        choices=stage_choices,
    ).ask()

    if stage is None:
        print("Cancelled.")
        return

    sys.exit(run_stage(stage, extra))


if __name__ == "__main__":
    main()
