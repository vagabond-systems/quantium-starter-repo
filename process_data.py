import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv", sep=",", engine="python")
df2 = pd.read_csv("data/daily_sales_data_1.csv", sep=",", engine="python")
df3 = pd.read_csv("data/daily_sales_data_2.csv", sep=",", engine="python")

df = pd.concat([df1, df2, df3])

df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns)

# HANDLE BAD HEADER CASE
if len(df.columns) == 1:
    df = df[df.columns[0]].str.split(",", expand=True)
    df.columns = ["product", "price", "quantity", "date", "region"]

# Continue normally
df = df[df["product"].str.lower() == "pink morsel"]

df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)

df["quantity"] = pd.to_numeric(df["quantity"], errors='coerce')

df = df.dropna()

df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("formatted_sales_data.csv", index=False)

print(" Done!")