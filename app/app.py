import pandas as pd
import glob

# Load all CSV files from data folder (assumes three files)
files = glob.glob('data/*.csv')
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# Filter for Pink Morsels only
df = df[df['product'] == 'Pink Morsel']

# Compute sales value
df['sales'] = df['quantity'] * df['price']

# Select and aggregate relevant fields: sum sales by DATE and REGION
output_df = df.groupby(['DATE', 'REGION'])['sales'].sum().reset_index()

# Save single output CSV
output_df.to_csv('processed_sales_data.csv', index=False)
