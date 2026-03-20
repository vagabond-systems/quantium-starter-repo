import pandas as pd
import os

# Define the paths
data_dir = "data"
output_file = "pink_morsel_sales.csv"

# List to store dataframes
processed_data = []

# Iterate through all files in the data directory
for filename in os.listdir(data_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_dir, filename)
        
        # Read the csv file
        df = pd.read_csv(file_path)
        
        # Filter for "pink morsel" (case-insensitive just in case, though schema showed lowercase)
        df_filtered = df[df['product'].str.lower() == "pink morsel"].copy()
        
        # Clean price (remove "$" and convert to float)
        df_filtered['price'] = df_filtered['price'].replace(r'[\$,]', '', regex=True).astype(float)
        
        # Calculate sales (price * quantity)
        df_filtered['sales'] = df_filtered['price'] * df_filtered['quantity']
        
        # Select required columns
        df_result = df_filtered[['sales', 'date', 'region']]
        
        processed_data.append(df_result)

# Concatenate all processed dataframes
final_df = pd.concat(processed_data, ignore_index=True)

# Save to csv
final_df.to_csv(output_file, index=False)

print(f"Data processing complete. Saved {len(final_df)} rows to {output_file}.")
