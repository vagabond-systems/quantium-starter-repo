import pandas as pd
from pathlib import Path

# Find all CSV files in the data folder
data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

# Read all files and combine them
df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove the dollar sign from price
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Calculate sales
df["Sales"] = df["quantity"] * df["price"]

# Keep only the required columns
output = df[["Sales", "date", "region"]]

# Rename columns
output.columns = ["Sales", "Date", "Region"]

# Save the result
output.to_csv("formatted_output.csv", index=False)

print("Done! formatted_output.csv has been created.")