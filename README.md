# Dev Box Setup

A Python CLI that installs ~120 packages on a fresh Ubuntu dev box via a 4-stage pipeline: **Install → Login → Pull → Config**.

## Prerequisites

```bash
pip install questionary pyyaml
```

## Usage

| Command | Effect |
|---------|--------|
| `python3 setup.py` | TUI — pick a stage, select packages via checkbox |
| `python3 setup.py --all` | Run all 4 stages, skip interactive packages |
| `python3 setup.py --unattended` | Same as `--all`, exit non-zero on failure |
| `python3 setup.py --select git,gh` | Install specific packages by name |
| `python3 setup.py --list` | Show all packages grouped by stage |
| `python3 setup.py --dry-run` | Preview commands without executing |
| `python3 setup.py --stage 2` | Run a single stage (TUI) |
| `python3 setup.py --from-stage 3` | Run from stage N onward |
| `python3 setup.py --packages-dir <dir>` | Use a custom packages directory |

## Adding a Package

Append an entry to the correct type file in `packages/` (e.g. `packages/apt.yaml`). Each file has a top-level `packages:` key. Validate your changes with `--list` and `--dry-run` before running for real.

- `check` commands must exit 0 if the package is already present. If omitted, the package always runs.
- `interactive: true` packages are skipped in `--all` / `--unattended` mode.
- `depends_on` is resolved via topological sort; deps must exist in the same selected set.

## Architecture

- `setup.py` — single-file CLI
- `packages/` — YAML definitions merged at runtime:
  - `_stages.yaml` — stage order and descriptions
  - `apt.yaml`, `snap.yaml`, `script.yaml`, `pip.yaml`, `npm.yaml`, `go.yaml`, `manual.yaml` — packages grouped by install type
