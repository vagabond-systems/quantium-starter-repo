from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/processed/pink_morsels_sales.csv")


def load_data(path: Path | str = DATA_PATH):
    """Load raw sales data and parse dates. Returns the unaggregated DataFrame.

    Keep the raw rows so callers can filter by region before aggregating.
    """
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def daily_sales_by_region(df: pd.DataFrame, region: str = 'all') -> pd.DataFrame:
    """Aggregate daily sales for a given region.

    region: one of 'north','east','south','west','all' (case-insensitive)
    """
    if region and region.lower() != 'all':
        if 'Region' in df.columns:
            # build a clear pandas boolean mask; handle NaNs safely by filling
            # with empty string before lowercasing
            mask = df['Region'].fillna('').str.lower() == region.lower()
            df = df[mask]

    daily = df.groupby('Date', as_index=False)['Sales'].sum()
    daily = daily.sort_values('Date')
    return daily
