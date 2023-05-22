#!/bin/bash

# Activate the project virtual environment
source venv/bin/activate

# Execute the test suite
pytest

# Return exit code 0 if all tests passed, or 1 if something went wrong
exit $?