# Dev Box Setup CLI

## Goal
A single command to reproducibly set up a fresh Ubuntu dev box with all required tools. Should work interactively (TUI checkbox picker) and in unattended mode (for `curl | bash` bootstrapping).

## Architecture

```
packages.yaml          # Declarative package manifest
setup.py               # Python CLI runner
bootstrap.sh           # (future) curl-pipeable entrypoint: installs python, pulls YAML, runs setup.py --unattended
```

## Package Definition (YAML)

Each entry:
- `name`: slug used as key
- `description`: human-readable
- `category`: grouping for TUI (system, dev-tools, infrastructure, networking, ai, utils)
- `type`: install method (`apt`, `snap`, `script`, `manual`)
- `package`: apt/snap package name
- `check`: command to verify already-installed (exit 0 = installed, skip)
- `commands`: list of shell commands to install
- `post_install`: list of commands to run after install (e.g. `gh auth login`)
- `interactive`: bool — if true, requires user input (auth, password). Skipped in unattended mode.
- `depends_on`: list of package names that must install first

## CLI Modes

### Interactive (default)
- Shows categorized checkbox menu via `questionary`
- User selects packages, confirms, then runs
- Interactive steps pause for user input

### Unattended (`--all` or `--unattended`)
- Installs everything except `interactive: true` packages
- Non-zero exit on failures
- Prints a final "run these manually" list for interactive packages

### Headless (`--select pkg1,pkg2,pkg3`)
- Installs only named packages, no TUI

## Future: Bootstrap Flow
User runs: `curl -sL setup.jimmyb.co.za | bash`
- bootstrap.sh downloads packages.yaml and setup.py
- Installs `python3` and `pip3` if missing
- `pip install questionary pyyaml`
- Runs `python3 setup.py --all`
- Reports what needs manual intervention

## Priorities
1. PRD & project structure
2. `packages.yaml` with packages from bash history
3. `setup.py` with TUI and runner logic
4. Test on fresh box
5. `bootstrap.sh` for curl-pipeable setup
