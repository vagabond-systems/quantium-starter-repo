# Quantium Challenge
This repo contains everything you need to get started on the program! Good luck!

## References
- [Check the Quantium Challenge Yourself!](https://www.theforage.com/simulations/quantium/software-engineering-j6ci)
- [Docs for this project](/quantium-starter-repo/_docs)

## Skills to be learnt/tested
- Python
- Virtual environment
- Data management
- Dashboard tools
- Data analysis
- CSS
- Python testing
- Test automation
- Shell scripting

## Data processing script
Run it to generate a single cleaned CSV for Pink Morsels sales.

The script is idempotent and will create the `data/processed/` folder if missing.

## How to run the Dash app

1. Install dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

3. Open the app in your browser at `http://127.0.0.1:8050`.

The app reads the single processed source of truth at `data/processed/pink_morsels_sales.csv`.

## Running tests

Before running tests locally or in CI, install the package in editable mode so tests import the real package:

```bash
pip install -e .
pip install -r requirements.txt
```

Run the test suite with:

```bash
pytest -q
```

---

## Task status

- **Tasks 1–5 completed:** data processing, aggregation, Dash visualiser, UI/CSS improvements and tests
- **Dashboard entrypoint:** `app.py` (run with `python app.py`).
- **Data source:** `data/processed/pink_morsels_sales.csv` (single source of truth).