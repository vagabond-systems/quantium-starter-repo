import pandas as pd
import numpy as np
import glob

# Read and combine all local CSVs with the same schema
files = sorted(glob.glob('data/daily_sales_data_*.csv'))
if files:
    df_list = [pd.read_csv(f) for f in files]
    # ensure we only concat dataframes with the expected columns
    df = pd.concat(df_list, ignore_index=True, sort=False)
else:
    # fallback if no files found
    df = pd.DataFrame(columns=['product', 'price', 'quantity', 'date', 'region'])

# normalize product names (strip + lower) to make the filter robust
if 'product' in df.columns:
    df['product'] = df['product'].astype(str).str.strip()
else:
    df['product'] = ''

# parse price (remove $ and convert to float) and quantity to numeric
def parse_price(x):
    try:
        return float(str(x).replace('$', '').replace(',', '').strip())
    except Exception:
        return np.nan

df['price'] = df['price'].apply(parse_price) if 'price' in df.columns else np.nan
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce') if 'quantity' in df.columns else np.nan

# filter case-insensitively for pink morsel
pink_mask = df['product'].str.lower() == 'pink morsel'
df = df[pink_mask]

# compute sales safely
df['sales'] = df['price'] * df['quantity']

# drop the original price and quantity columns if they exist
cols_to_drop = [c for c in ['price', 'quantity'] if c in df.columns]
if cols_to_drop:
    df = df.drop(columns=cols_to_drop)

# basic logging: write out counts to stdout
print(f"Found {len(files)} input files. Combined rows: {sum(len(d) for d in df_list) if files else 0}")
print(f"Filtered rows (pink morsel): {len(df)}")

# output the processed data to a new CSV
df.to_csv('data/processed_sales_data.csv', index=False)