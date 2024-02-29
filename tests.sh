#!/bin/bash

source venv/Scripts/activate
pytest
pytest_exit_code=$?
echo $?
deactivate

