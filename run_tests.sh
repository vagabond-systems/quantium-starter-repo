#!/bin/bash

# 1. Activate the virtual environment
# Note: This assumes your venv is named 'venv'
source venv/Scripts/activate

# 2. Execute the test suite
# We use pytest to run the tests we created in Task 5
pytest test_app.py

# 3. Capture the exit code of the last command
test_result=$?

# 4. Return 0 if passed, 1 if failed
if [ $test_result -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed. Please check the logs."
    exit 1
fi
