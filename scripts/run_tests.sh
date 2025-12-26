#!/usr/bin/env bash
# Run the project's test suite in an isolated virtual environment.
# Exits with 0 on success, 1 on failure.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Prefer an already activated venv. Otherwise use .venv or venv or create .venv.
if [ -n "${VIRTUAL_ENV:-}" ]; then
  echo "Using active virtualenv: ${VIRTUAL_ENV}"
else
  if [ -d ".venv" ]; then
    echo "Activating .venv"
    # shellcheck disable=SC1091
    source .venv/bin/activate
  elif [ -d "venv" ]; then
    echo "Activating venv"
    # shellcheck disable=SC1091
    source venv/bin/activate
  else
    echo "No virtualenv found — creating .venv and installing requirements"
    python -m venv .venv
    # shellcheck disable=SC1091
    source .venv/bin/activate
    pip install --upgrade pip
    if [ -f requirements.txt ]; then
      pip install -r requirements.txt
    fi
  fi
fi

# Ensure package is installed in editable mode so tests import real package
pip install -e . >/dev/null

echo "Running pytest..."
if pytest -q; then
  echo "All tests passed"
  exit 0
else
  echo "Tests failed" >&2
  exit 1
fi
