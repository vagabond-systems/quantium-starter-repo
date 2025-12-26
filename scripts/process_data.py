from pathlib import Path
import pandas as pd
import sys


def find_column(df, candidates):
    cols = {c.lower(): c for c in df.columns}
    for name in candidates:
        if name.lower() in cols:
            return cols[name.lower()]
    return None


def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    out_dir = data_dir / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "pink_morsels_sales.csv"

    csvs = sorted(data_dir.glob("daily_sales_data_*.csv"))
    if not csvs:
        print("No input CSV files found in data/", file=sys.stderr)
        sys.exit(2)

    dfs = []
    for p in csvs:
        try:
            df = pd.read_csv(p)
        except Exception as e:
            print(f"Failed to read {p}: {e}", file=sys.stderr)
            continue
        dfs.append(df)

    if not dfs:
        print("No dataframes loaded; exiting.", file=sys.stderr)
        sys.exit(3)

    df = pd.concat(dfs, ignore_index=True, sort=False)

    # Locate expected columns robustly
    product_col = find_column(df, ["product", "Product"])
    qty_col = find_column(df, ["quantity", "qty", "Quantity"])
    price_col = find_column(df, ["price", "Price"])
    date_col = find_column(df, ["date", "Date"])
    region_col = find_column(df, ["region", "Region"])

    if product_col is None:
        print("Could not find a 'product' column in the input files.", file=sys.stderr)
        sys.exit(4)
    if qty_col is None or price_col is None:
        print("Could not find 'quantity' or 'price' columns.", file=sys.stderr)
        sys.exit(5)
    if date_col is None:
        print("Could not find a 'date' column; continuing but dates may be empty.", file=sys.stderr)

    # Filter to Pink Morsels. Try exact match first, then case-insensitive variants,
    # then a fallback that matches product names containing both words.
    prod_series = df[product_col].astype(str).str.strip()
    mask = prod_series == "Pink Morsels"
    if mask.sum() == 0:
        mask = prod_series.str.lower().isin(["pink morsel", "pink morsels"])
    if mask.sum() == 0:
        mask = prod_series.str.lower().str.contains("pink") & prod_series.str.lower().str.contains("morsel")
    if mask.sum() == 0:
        sample = prod_series.dropna().unique()[:10]
        print("No Pink Morsels rows found. Example product values:", sample, file=sys.stderr)

    df_filtered = df[mask].copy()

    # Ensure numeric for computation. Strip currency symbols/commas from price.
    df_filtered[qty_col] = pd.to_numeric(df_filtered[qty_col], errors="coerce").fillna(0)
    df_filtered[price_col] = (
        df_filtered[price_col].astype(str)
        .str.replace(r"[^0-9.\-]", "", regex=True)
    )
    df_filtered[price_col] = pd.to_numeric(df_filtered[price_col], errors="coerce").fillna(0)

    df_filtered["Sales"] = df_filtered[qty_col] * df_filtered[price_col]

    # Parse and normalize Date
    if date_col is not None:
        df_filtered["Date"] = pd.to_datetime(df_filtered[date_col], errors="coerce").dt.strftime("%Y-%m-%d")
    else:
        df_filtered["Date"] = ""

    # Region column fallback
    region_output_col = region_col if region_col is not None else None
    if region_output_col is None:
        df_filtered["Region"] = ""
    else:
        df_filtered["Region"] = df_filtered[region_output_col]

    out_df = df_filtered[["Sales", "Date", "Region"]]

    out_df.to_csv(out_file, index=False)

    print(f"Wrote {len(out_df)} rows to {out_file}")


if __name__ == "__main__":
    main()