import pandas as pd

# Load the three CSV files
file1 = pd.read_csv(r"D:\Python\Quantium\quantium-starter-repo-main\quantium-starter-repo-main\data\daily_sales_data_0.csv")
file2 = pd.read_csv(r"D:\Python\Quantium\quantium-starter-repo-main\quantium-starter-repo-main\data\daily_sales_data_1.csv")
file3 = pd.read_csv(r"D:\Python\Quantium\quantium-starter-repo-main\quantium-starter-repo-main\data\daily_sales_data_2.csv")

# Combine all files into one DataFrame
data = pd.concat([file1, file2, file3], ignore_index=True)

# Keep only Pink Morsels
data = data[data["product"] == "pink morsel"]

# Convert price from string to float
data["price"] = data["price"].replace(r'[\$,]', '', regex=True).astype(float)

# Create Sales column
data["Sales"] = data["price"] * data["quantity"]

# Select required columns and rename them
output = data[["Sales", "date", "region"]].rename(
    columns={
        "date": "Date",
        "region": "Region"
    }
)

# Export to CSV
output.to_csv(
    r"D:\Python\Quantium\quantium-starter-repo-main\quantium-starter-repo-main\data\formatted_output.csv",
    index=False
)
print("Output file created successfully!")