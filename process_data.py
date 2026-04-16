import pandas as pd

def main() -> None:
    files = [
        "data/daily_sales_data_0.csv",
        "data/daily_sales_data_1.csv",
        "data/daily_sales_data_2.csv",
    ]

    df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

    df = df[df["product"].str.strip().str.lower() == "pink morsel"].copy()
    df["price"] = df["price"].replace(r"[$,]", "", regex=True).astype(float)
    df["Sales"] = df["quantity"] * df["price"]

    output = df[["Sales", "date", "region"]].rename(
        columns={"date": "Date", "region": "Region"}
    )
    output.to_csv("data/formatted_output.csv", index=False)

if __name__ == "__main__":
    main()
