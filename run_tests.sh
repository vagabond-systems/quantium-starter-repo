#!/bin/bash
# Exit immediately if any command fails
set -e

# Activate the virtual environment
if [ -d ".quantium" ]; then
    source .quantium/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found."
    exit 1
fi

# Run pytest and capture exit status
pytest -v
TEST_RESULT=$?

# Handle exit codes
if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi