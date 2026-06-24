#!/usr/bin/env bash
# Dev Box Bootstrap
# Pipe-friendly: curl -fsSL https://raw.githubusercontent.com/James-Burgess/dev-setup/master/bootstrap.sh | bash
#
# Clones the dev-setup repo into /tmp, creates a venv to run setup.py
# (needs yaml + questionary). Pip packages are installed for the user,
# not inside the venv.

set -e

REPO_URL="https://github.com/James-Burgess/dev-setup.git"
REPO_DIR="/tmp/dev-setup"

fail_count=0

# ── Clone / update dev-setup repo ──────────────────────────────────────────────
if ! command -v git &>/dev/null; then
    echo "[bootstrap] git not found — installing..."
    sudo apt-get update && sudo apt-get install -y git || { echo "[bootstrap] Failed to install git"; ((fail_count++)); }
fi

if [ ! -d "$REPO_DIR/.git" ]; then
    echo "[bootstrap] Cloning dev-setup into $REPO_DIR..."
    git clone "$REPO_URL" "$REPO_DIR" || { echo "[bootstrap] Failed to clone repo"; ((fail_count++)); }
else
    echo "[bootstrap] dev-setup already exists at $REPO_DIR, updating..."
    git -C "$REPO_DIR" pull || echo "[bootstrap] Could not update (continuing with existing copy)"
fi

cd "$REPO_DIR" || { echo "[bootstrap] Repo directory not found"; exit 1; }

# ── Ensure system Python and venv tooling ──────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "[bootstrap] python3 not found — installing..."
    sudo apt-get update && sudo apt-get install -y python3 || { echo "[bootstrap] Failed to install python3"; ((fail_count++)); }
fi

if ! virtualenv --help &>/dev/null; then
    echo "[bootstrap] python3-venv not found — installing..."
    sudo apt-get update && sudo apt-get install -y virtualenv || { echo "[bootstrap] Failed to install python3-venv"; ((fail_count++)); }
fi

# ── Create/refresh venv just for setup.py runtime ──────────────────────────────
VENV_DIR=".bootstrap-venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "[bootstrap] Creating virtual environment in $VENV_DIR..."
    virtualenv "$VENV_DIR" || { echo "[bootstrap] Failed to create venv"; ((fail_count++)); }
fi

# Install runtime deps into the venv
"$VENV_DIR/bin/pip" install pyyaml questionary || { echo "[bootstrap] Failed to install deps into venv"; ((fail_count++)); }

# ── Launch interactive setup ────────────────────────────────────────────────────
if [ "$fail_count" -gt 0 ]; then
    echo "[bootstrap] $fail_count step(s) failed. Setup may not work correctly."
fi

echo "[bootstrap] Starting interactive setup..."
"$VENV_DIR/bin/python" setup.py

exit 0
