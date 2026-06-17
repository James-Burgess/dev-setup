# Dev Box Setup — Agent Guide

## What this is
A Python CLI that installs ~120 packages on a fresh Ubuntu dev box via a multi-stage pipeline. Three stages exist: Install, Login, and Configure.

## Commands

| Command | Effect |
|---------|--------|
| `python3 setup.py` | TUI — pick a stage, then select packages via checkbox |
| `python3 setup.py --all` | Run all stages, skip interactive steps |
| `python3 setup.py --unattended` | Same as `--all`, exit non-zero on failure |
| `python3 setup.py --select git,gh` | Install specific packages by name |
| `python3 setup.py --list` | List packages grouped by source file |
| `python3 setup.py --dry-run` | Preview commands without executing |
| `python3 setup.py --stage 2` | Run a single stage |
| `python3 setup.py --from-stage 2` | Run from stage N onward |
| `python3 --packages-dir <dir>` | Override default `packages/` directory |

## Dependencies
- Runtime: `python3`, `pyyaml`
- TUI mode: `questionary` (`pip install questionary pyyaml`)

## Architecture

```
setup.py                 # Orchestrator — maps stage numbers to script paths
stage_1_install.py       # Package installation from YAML manifests
stage_2_login.py         # Authenticate to services (gh auth login)
stage_3_configure.py     # Shell, dotfiles, and system settings
packages/                # YAML manifests grouped by tool domain
  *.yaml                 # Domain files (system.yaml, dev-tools.yaml, ai.yaml, …)
bin/                     # Bundled helper scripts (e.g. chezmoi)
bootstrap.sh             # Creates venv, installs deps, runs setup.py
```
- `setup.py` sets `GOBIN=~/go/bin`, `GOPATH=~/go`, and prepends both `~/go/bin` and `~/.local/bin` to `PATH` so Go-installed tools are discoverable by `check` commands across stages. `stage_1_install.py` does the same when run directly.
- Package YAML files are loaded by their `type` field (`apt`, `snap`, `pip`, `npm`, `go`, `cargo`, `script`, `manual`). The source filename becomes each entry's `source` field for grouping in `--list`.
- Stage scripts all accept the same CLI args (`--select`, `--packages-dir`, `--list`, `--dry-run`, `--unattended`) — even as no-ops — so the orchestrator can pass them through without errors.

## Configuration & Dotfiles

- **Chezmoi** manages dotfiles via `~/.local/share/chezmoi`. Key files:
  - `dot_zshenv` — bootstraps `ZDOTDIR` to `~/.config/zsh`
  - `private_dot_config/zsh/dot_zshenv` — sets `GOPATH`, `GOBIN`, `PATH`, and other env vars
  - `private_dot_config/zsh/dot_zshrc` — shell config, aliases, plugin loading
- The orchestrator (`setup.py`) and stage scripts must not overwrite or conflict with chezmoi-managed files. If you change shell config (`.zshenv`, `.zshrc`), apply the change via chezmoi (`chezmoi add <file>` in `~/.local/share/chezmoi`) so it persists across re-clones.
- `stage_3_configure.py` runs `chezmoi apply` as part of the pipeline to sync dotfiles to `$HOME`.

## Conventions
- **Adding a package**: append an entry to the domain YAML file in `packages/` (e.g. `packages/dev-tools.yaml`). Top-level key is `packages:`.
- `check` must exit 0 if already present. Omitting `check` means always re-run.
- `interactive: true` packages/steps are skipped in `--all` / `--unattended` mode.
- `depends_on` is topologically sorted; deps must exist in the same selected set.
- **No tests, CI, or formatter**. Validate changes by running `--list` and `--dry-run` before real execution.
