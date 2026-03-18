#!/usr/bin/bash

# run_tests.sh - CI/CD test automation for Soul Foods Dash app
set -e  # Exit on any error

echo " Starting Soul Foods Pink Morsel Dashboard test suite..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo -e "${YELLOW}Activating virtual environment...${NC}"
    source venv/bin/activate
else
    echo -e "${RED}ERROR: Virtual environment 'venv' not found!${NC}"
    echo "Run: python -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Verify required files exist
for file in app.py test_app.py processed_sales_data.csv requirements.txt; do
    if [ ! -f "$file" ]; do
        echo -e "${RED}ERROR: Missing required file: $file${NC}"
        exit 1
    fi
done

# Install/upgrade testing dependencies
echo -e "${YELLOW}Installing test dependencies...${NC}"
pip install --upgrade pytest dash[testing] pytest-xdist

# Run test suite
echo -e "${YELLOW}Running test suite...${NC}"
pytest test_app.py \
    -v \
    --tb=short \
    --maxfail=1 \
    --strict-markers \
    || {
    echo -e "${RED} TESTS FAILED - CI pipeline aborted${NC}"
    exit 1
}

echo -e "${GREEN} All tests PASSED successfully!${NC}"
echo -e "${GREEN} Dashboard is production-ready${NC}"
exit 0
