# Wrapper Script for Quantium Data Analysis Dashboard

Write-Host "Starting Data Processing..." -ForegroundColor Cyan
.\venv\Scripts\python.exe process_data.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "Data processing failed. Aborting." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "Running Automated Tests..." -ForegroundColor Cyan
.\venv\Scripts\pytest -v test_app.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed. Please check test_app.py." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "Launching Visualization Dashboard..." -ForegroundColor Green
.\venv\Scripts\python.exe app.py
