import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSVs and concatenate into one DataFrame
files = list(data_path.glob("*.csv"))
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# Filter for Pink Morsel only
df = df[df['product'] == 'pink morsel']

# Calculate total sales
df['sales'] = df['quantity'] * df['price']

# Keep only required columns
output = df[['sales', 'date', 'region']]

# Save processed output
output_path = Path("processed_data")
output_path.mkdir(exist_ok=True)
output.to_csv(output_path / "pink_morsel_sales.csv", index=False)

print("Processed data saved to processed_data/pink_morsel_sales.csv")