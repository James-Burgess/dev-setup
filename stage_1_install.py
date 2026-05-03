#!/usr/bin/env python3
"""
Dev Box Setup — install packages from YAML manifests.

Usage:
  python3 setup.py                      TUI — select packages via checkbox
  python3 setup.py --all                Install all packages, skip interactive
  python3 setup.py --unattended         Same as --all, exit non-zero on failure
  python3 setup.py --select git,gh      Install specific packages by name
  python3 setup.py --list               List all packages grouped by category
  python3 setup.py --dry-run            Preview commands without executing
"""

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DIR = SCRIPT_DIR / "packages"

packages_dir: Path = DEFAULT_DIR


# ═══════════════════════════════════════════════════════════════════════════════
# YAML loading
# ═══════════════════════════════════════════════════════════════════════════════

def load_manifest():
    """Returns packages by merging all .yaml files in packages_dir."""
    try:
        import yaml
    except ImportError:
        print("✗ pyyaml is required.", file=sys.stderr)
        print("   Install it with: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    all_packages = []

    yaml_files = sorted(packages_dir.glob("*.yaml"))
    if not yaml_files:
        print(f"✗ No .yaml files found in {packages_dir}", file=sys.stderr)
        sys.exit(1)

    for yf in yaml_files:
        with open(yf) as f:
            data = yaml.safe_load(f) or {}
        source = yf.stem
        for pkg in data.get("packages", []):
            pkg.setdefault("source", source)
            all_packages.append(pkg)

    if not all_packages:
        print(f"✗ No packages loaded from {packages_dir}", file=sys.stderr)
        sys.exit(1)

    return all_packages


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════

def is_installed(pkg):
    check = pkg.get("check", "")
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


def _find_cmd(name):
    try:
        subprocess.run(["which", name], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def resolve_order(selected):
    """Topological sort respecting depends_on (all deps must be in selected set)."""
    name_to_pkg = {p["name"]: p for p in selected}
    resolved = []
    seen = set()
    visiting = set()

    def visit(name):
        if name in seen:
            return
        if name in visiting:
            print(f"⚠  Circular dependency: {name}", file=sys.stderr)
            return
        visiting.add(name)
        pkg = name_to_pkg.get(name)
        if pkg:
            for dep in pkg.get("depends_on", []):
                if dep in name_to_pkg:
                    visit(dep)
        visiting.discard(name)
        if name in name_to_pkg:
            resolved.append(name)
            seen.add(name)

    for name in name_to_pkg:
        visit(name)

    return [name_to_pkg[n] for n in resolved]


# ═══════════════════════════════════════════════════════════════════════════════
# Package installer
# ═══════════════════════════════════════════════════════════════════════════════

def install_package(pkg, unattended=False, dry_run=False):
    name = pkg["name"]
    source = pkg.get("source", "?")
    print(f"\n─── {name} [{source}] ────────────────────")

    if is_installed(pkg):
        print(f"  ✓ Already installed — skipping")
        return True

    if pkg.get("interactive") and unattended:
        print(f"  ⚠  Interactive — skipping in unattended mode")
        return "skipped_interactive"

    commands = pkg.get("commands", [])
    pkg_type = pkg["type"]
    pkg_name = pkg.get("package", name)

    if not commands:
        if pkg_type == "apt":
            commands = [f"sudo apt install -y {pkg_name}"]
        elif pkg_type == "snap":
            flags = " --classic" if "classic" in (pkg.get("snap_flags") or "") else ""
            commands = [f"sudo snap install {pkg_name}{flags}"]
        elif pkg_type == "pip":
            commands = [f"pip3 install --user --break-system-packages {pkg_name}"]
        elif pkg_type == "npm":
            commands = [f"npm install -g {pkg_name}"]
        elif pkg_type == "go":
            commands = [f"go install {pkg_name}@latest"]
        elif pkg_type == "cargo":
            commands = [f"cargo install {pkg_name}"]

    if dry_run:
        for c in commands:
            print(f"  [dry-run] → {c}")
        for c in pkg.get("post_install", []):
            print(f"  [dry-run] → {c}")
        return True

    for cmd in commands:
        if not run_cmd(cmd):
            print(f"  ✗ Failed: {cmd}")
            return False

    post = pkg.get("post_install", [])
    if post and pkg.get("interactive") and unattended:
        print("  ⚠  post_install skipped (interactive)")
        return "skipped_post"
    for cmd in post:
        if not run_cmd(cmd):
            print(f"  ✗ post_install failed: {cmd}")
            return False

    print(f"  ✓ Done")
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# Runner
# ═══════════════════════════════════════════════════════════════════════════════

def run_install_list(ordered, unattended=False, dry_run=False):
    failed = []
    skipped = []
    ok = 0

    for pkg in ordered:
        result = install_package(pkg, unattended=unattended, dry_run=dry_run)
        if result is True:
            ok += 1
        elif result == "skipped_interactive":
            skipped.append(pkg["name"])
        elif result == "skipped_post":
            skipped.append(pkg["name"] + " (post-install)")
        else:
            failed.append(pkg["name"])

    return {"ok": ok, "failed": failed, "skipped": skipped}


def print_results(results):
    print(f"\n{'─' * 55}")
    print(f"  {results['ok']} ok, {len(results['failed'])} failed, {len(results['skipped'])} skipped")

    if results["skipped"]:
        print("\nSkipped (needs manual run):")
        for s in results["skipped"]:
            print(f"  - {s}")
    if results["failed"]:
        print("\nFailed:")
        for f in results["failed"]:
            print(f"  - {f}")

    return len(results["failed"]) == 0


# ═══════════════════════════════════════════════════════════════════════════════
# TUI
# ═══════════════════════════════════════════════════════════════════════════════

def tui_select_packages(packages):
    """Show checkbox picker grouped by source file and install selected packages."""
    import questionary

    by_source = {}
    for p in packages:
        src = p.get("source", "other")
        by_source.setdefault(src, []).append(p)

    choices = []
    for src, pkgs in sorted(by_source.items()):
        choices.append(questionary.Separator(f"── {src} ──"))
        for p in pkgs:
            already = " ✓" if is_installed(p) else ""
            title = f"{p['name']:28s}  {p.get('description', '')}{already}"
            choices.append(questionary.Choice(title=title, value=p["name"]))

    selected = questionary.checkbox(
        "Select packages (space to toggle, enter to confirm):",
        choices=choices,
        instruction="(↑↓ move, space toggle, enter confirm)",
    ).ask()

    if selected is None:
        print("Cancelled.")
        return None
    if not selected:
        print("Nothing selected.")
        return None

    selected_pkgs = [p for p in packages if p["name"] in selected]
    ordered = resolve_order(selected_pkgs)

    print("\nInstalling in order:")
    for p in ordered:
        print(f"  • {p['name']}")
    print()

    confirm = questionary.confirm("Proceed with installation?", default=True).ask()
    if not confirm:
        print("Aborted.")
        return None

    return ordered


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    global packages_dir

    parser = argparse.ArgumentParser(
        description="Dev Box Setup — install packages from YAML manifests"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="Install all packages, skip interactive")
    group.add_argument("--select", type=str, help="Comma-separated package names")
    group.add_argument("--list", action="store_true", help="List all packages grouped by source")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--unattended", action="store_true")
    parser.add_argument("--packages-dir", type=str, default=str(DEFAULT_DIR), help="Directory containing package .yaml files")
    args = parser.parse_args()

    packages_dir = Path(args.packages_dir)
    if not packages_dir.is_dir():
        print(f"✗ packages directory not found at {packages_dir}", file=sys.stderr)
        sys.exit(1)

    packages = load_manifest()
    if not packages:
        print("✗ No packages loaded from YAML", file=sys.stderr)
        sys.exit(1)

    unattended = args.unattended

    # ── --list ────────────────────────────────────────────────────────────────

    if args.list:
        by_source = {}
        for p in packages:
            src = p.get("source", "?")
            by_source.setdefault(src, []).append(p)

        for src, pkgs in sorted(by_source.items()):
            print(f"\n═══ {src}")
            for p in pkgs:
                tag = "⚡" if p.get("interactive") else "  "
                ok = "✓" if is_installed(p) else " "
                print(f"  {tag}[{ok}] {p['name']:28s} [{p.get('type', '?'):7s}]  {p.get('description', '')}")
        sys.exit(0)

    # ── --select ──────────────────────────────────────────────────────────────

    if args.select:
        wanted = [n.strip() for n in args.select.split(",")]
        selected = [p for p in packages if p["name"] in wanted]
        if not selected:
            print(f"No matching packages for: {args.select}")
            sys.exit(1)
        ordered = resolve_order(selected)
        results = run_install_list(ordered, unattended=unattended, dry_run=args.dry_run)
        success = print_results(results)
        sys.exit(0 if success else 1)

    # ── --all / --unattended ───────────────────────────────────────────────────

    if args.all or args.unattended:
        unattended = True
        to_install = [p for p in packages if not p.get("interactive")]
        print(f"Installing {len(to_install)} non-interactive packages...")
        ordered = resolve_order(to_install)
        results = run_install_list(ordered, unattended=unattended, dry_run=args.dry_run)
        success = print_results(results)
        sys.exit(0 if success else 1)

    # ── default TUI ───────────────────────────────────────────────────────────

    ordered = tui_select_packages(packages)
    if ordered is None:
        return

    results = run_install_list(ordered, unattended=False, dry_run=args.dry_run)
    print_results(results)


if __name__ == "__main__":
    main()
