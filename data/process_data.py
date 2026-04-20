import pandas as pd

# Load files
df1 = pd.read_csv("daily_sales_data_0.csv")
df2 = pd.read_csv("daily_sales_data_1.csv")
df3 = pd.read_csv("daily_sales_data_2.csv")

# Combine
df = pd.concat([df1, df2, df3])

# Filter pink morsels
df = df[df["product"].str.lower() == "pink morsel"]

# 🔥 FIX: clean the price column
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Ensure quantity is numeric (just in case)
df["quantity"] = df["quantity"].astype(float)

# Create sales
df["sales"] = df["quantity"] * df["price"]

# Keep required columns
df = df[["sales", "date", "region"]]

# Save output
df.to_csv("formatted_sales_data.csv", index=False)

print("Data processing complete ✅")