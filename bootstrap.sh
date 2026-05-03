#!/usr/bin/env bash
# Dev Box Bootstrap
# Creates a venv to run setup.py (needs yaml + questionary), but pip packages
# are installed for the user, not inside the venv.

cd "$(dirname "$0")" || exit

fail_count=0

# ── Ensure system Python and venv tooling ────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "[bootstrap] python3 not found — installing..."
    sudo apt-get update && sudo apt-get install -y python3 || { echo "[bootstrap] Failed to install python3"; ((fail_count++)); }
fi

if ! virtualenv --help &>/dev/null; then
    echo "[bootstrap] python3-venv not found — installing..."
    sudo apt-get update && sudo apt-get install -y virtualenv || { echo "[bootstrap] Failed to install python3-venv"; ((fail_count++)); }
fi

# ── Create/refresh venv just for setup.py runtime ────────────────────────────
VENV_DIR=".bootstrap-venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "[bootstrap] Creating virtual environment in $VENV_DIR..."
    virtualenv "$VENV_DIR" || { echo "[bootstrap] Failed to create venv"; ((fail_count++)); }
fi

# Install runtime deps into the venv
"$VENV_DIR/bin/pip" install pyyaml questionary || { echo "[bootstrap] Failed to install deps into venv"; ((fail_count++)); }

# ── Launch interactive setup ──────────────────────────────────────────────────
if [ "$fail_count" -gt 0 ]; then
    echo "[bootstrap] $fail_count step(s) failed. Setup may not work correctly."
fi

echo "[bootstrap] Starting interactive setup..."
"$VENV_DIR/bin/python" setup.py

exit 0
