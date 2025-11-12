#!/usr/bin/env bash

# Activate the project's virtual environment, run the test_dash_app.py test suite,
# and exit with 0 on success or 1 on any failure.

set -o pipefail

# Determine root project (prefer Git root if available, else current directory

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

# Locate a virtual environment (common names)
VENV_DIR=""
for dir in ".venv" "venv" "env" "ENV" "dev_venv"; do
  if [ -d "$PROJECT_ROOT/$dir" ]; then
    VENV_DIR="$PROJECT_ROOT/$dir"
    break
  fi
done

if [ -z "$VENV_DIR" ]; then
  echo "No virtual environment directory found in $PROJECT_ROOT (searched: .venv, venv, env, ENV, dev_venv)">&2
  exit 1
fi

# Activate the virtual environment
if [ -f "$VENV_DIR/bin/activate" ]; then
  # Linux/macOS
  source "$VENV_DIR/bin/activate"
  echo "Activated virtual environment: $VENV_DIR (Linux/macOS)"
elif [ -f "$VENV_DIR/Scripts/activate" ]; then
  # Windows (Git Bash / WSL)
  source "$VENV_DIR/Scripts/activate"
  echo "Activated virtual environment: $VENV_DIR (Windows)"
else
  echo "Activation script not found in $VENV_DIR" >&2
  exit 1
fi

# Ensure pytest is available in the activated environment
if ! command -v pytest >/dev/null 2>&1; then
  echo "pytest is not installed in the activated environment." >&2
  exit 1
fi

# Run the test suite
TEST_FILE="$PROJECT_ROOT/test_dash_app.py"
if [ -f "$TEST_FILE" ]; then
  echo "Running tests from $TEST_FILE"
  pytest -q "$TEST_FILE"
else
  echo "Test file not found at $TEST_FILE. Running pytest for all tests."
  pytest -q
fi

EXIT_CODE=$?

if [ "$EXIT_CODE" -eq 0 ]; then
  echo "Test suite passed."
  exit 0
else
  echo "Test suite failed or could not be executed. Exit code: $EXIT_CODE" >&2
  exit 1
fi


