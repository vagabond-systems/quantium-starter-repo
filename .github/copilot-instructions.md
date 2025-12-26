<!-- Copilot instructions tailored for the Quantium starter repo -->
# Copilot / AI agent instructions

Purpose: help an AI coding agent be productive quickly in this repository.

- **Big picture**: This is a small Dash-based visualiser that reads a single
  processed CSV and renders a Plotly time-series. The entrypoint is
  [app.py](app.py) which calls `create_app()` from the `pink_morsels` package.
  The `pink_morsels` package organizes responsibilities:
  - [pink_morsels/web.py](pink_morsels/web.py): Dash app layout, callbacks.
  - [pink_morsels/data.py](pink_morsels/data.py): data-loading and aggregation helpers.
  - [pink_morsels/viz.py](pink_morsels/viz.py): Plotly figure construction.

- **Source of truth**: processed data is expected at
  `data/processed/pink_morsels_sales.csv`. The repository includes a
  data-prep script: [scripts/process_data.py](scripts/process_data.py) — run it to
  regenerate the CSV from `data/daily_sales_data_*.csv`.

- **How to run locally**:
  - Create a venv and install deps: `pip install -r requirements.txt`.
  - Generate processed data (idempotent): `python scripts/process_data.py`.
  - Start the app: `python app.py` and visit http://127.0.0.1:8050.

- **Key patterns & conventions** (use these when editing or adding code):
  - Data API: `load_data()` returns unaggregated rows; callers should filter
    (e.g. by region) then aggregate via `daily_sales_by_region()` before plotting.
    See [pink_morsels/data.py](pink_morsels/data.py) for mask and grouping examples.
  - File paths use `pathlib.Path` and repository-relative paths (see
    [scripts/process_data.py](scripts/process_data.py)). Prefer Path-based operations.
  - Visualization: `make_figure()` expects a DataFrame with `Date` and `Sales`.
    Use pandas `Timestamp` when adding shapes/annotations so Plotly handles dates
    natively ([pink_morsels/viz.py](pink_morsels/viz.py)).
  - CSS & assets: Dash looks in the repo `assets/` folder; styles target stable
    `className` values (e.g. `region-radio`) in components (see
    [pink_morsels/web.py](pink_morsels/web.py) and [assets/style.css](assets/style.css)).

- **Data script behaviour to preserve**:
  - `scripts/process_data.py` tolerates varied column names (uses `find_column`).
  - It normalizes `Price` by stripping non-numeric characters, coerces numeric
    types and computes `Sales = quantity * price`, then writes `Sales,Date,Region`.
  - Keep the robust column-detection logic when refactoring or adding ETL steps.

- **Common edits you'll be asked to do**:
  - Add a new filter/control to the Dash layout: modify
    [pink_morsels/web.py](pink_morsels/web.py) and update `daily_sales_by_region`
    if the filter needs pre-aggregation logic.
  - Change the figure: modify [pink_morsels/viz.py](pink_morsels/viz.py) and ensure
    you maintain the `Date` dtype and any vertical marker logic.
  - Update data cleaning: change [scripts/process_data.py](scripts/process_data.py)
    and rerun the script to regenerate `data/processed/pink_morsels_sales.csv`.

- **Testing & debugging**:
  - There are no automated tests in the repo. For manual checks:
    - Run `python scripts/process_data.py` and inspect `data/processed/pink_morsels_sales.csv`.
    - Run `python app.py` (note `app.run(debug=True)` in `app.py`) and use browser dev tools.

- **What to avoid / project constraints**:
  - Do not change the single-source-of-truth output columns (`Sales,Date,Region`).
  - Avoid adding heavy runtime dependencies; this starter repo is intentionally small.

- **Where to look for examples**:
  - App entry: [app.py](app.py)
  - Dash layout & callbacks: [pink_morsels/web.py](pink_morsels/web.py)
  - Data functions: [pink_morsels/data.py](pink_morsels/data.py)
  - Plot construction: [pink_morsels/viz.py](pink_morsels/viz.py)
  - ETL script: [scripts/process_data.py](scripts/process_data.py)

If anything in this summary is unclear or you'd like more examples (tests,
CI commands, or PR guidance), tell me which section to expand.
