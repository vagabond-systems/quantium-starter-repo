import pandas as pd
import os

# Load all three CSV files from the data folder
data_folder = "data"
all_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

dfs = []
for file in all_files:
    df = pd.read_csv(os.path.join(data_folder, file))
    dfs.append(df)

# Combine into one dataframe
combined = pd.concat(dfs, ignore_index=True)

# Filter only Pink Morsels
combined = combined[combined["product"] == "pink morsel"]

# Calculate sales = quantity * price
combined["price"] = combined["price"].str.replace("$", "").astype(float)
combined["sales"] = combined["quantity"] * combined["price"]

# Keep only the required columns
output = combined[["sales", "date", "region"]]

# Save to output CSV
output.to_csv("data/output.csv", index=False)

print("Done! Output saved to data/output.csv")
print(output.head())