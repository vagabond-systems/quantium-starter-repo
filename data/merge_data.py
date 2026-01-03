import pandas as pd
import glob

# 1. Point to the data folder and find all sales CSVs
path = 'data/daily_sales_data_*.csv'
files = glob.glob(path)
print(f"Files found: {files}")

# 2. Combine all files
df_list = [pd.read_csv(f) for f in files]
merged_df = pd.concat(df_list, ignore_index=True)

# 3. Data Cleaning: Convert price string ($) to a number
merged_df['price'] = merged_df['price'].replace('[\$,]', '', regex=True).astype(float)

# 4. Calculate Revenue
merged_df['revenue'] = merged_df['quantity'] * merged_df['price']

# 5. Save the final file to the main folder
merged_df.to_csv('final_processed_data.csv', index=False)
print("Success! 'final_processed_data.csv' has been created.")