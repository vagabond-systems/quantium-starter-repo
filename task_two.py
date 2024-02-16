import pandas as pd
import glob


data_files = glob.glob("data/*.csv")


def task_two(product_name: str) -> None:
    """
    Filters data for a given product and calculates a sales column.
    """

    dataframes = []

    for file in data_files:
        df = pd.read_csv(file, converters={"price": lambda x: float(x.replace("$", ""))})

        processed_df = (df
            .loc[df["product"] == product_name]
            .assign(sales=lambda x: x["price"] * x["quantity"])
            .assign(sales=lambda x: x["sales"].map(lambda y: f"${y:.2f}"))
            [["sales", "date", "region"]]
        )

        dataframes.append(processed_df)

    output = pd.concat(dataframes)

    output.to_csv(f"output_files/{product_name}_sales.csv", index=False)


def main() -> None:
    task_two("pink morsel")


if __name__ == "__main__":
    main()
