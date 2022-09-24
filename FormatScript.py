import pandas as pd
import os

# Merge the 3 csv
# Make a new column sales before removing quantity & price & product
# Then write it to a new formated csv

def readCSV(path):
    df = pd.read_csv(path, delimiter=";", parse_dates=['date'], dayfirst=True)
    for x in df.index:
        if df.loc[x, 'product'] != "pink morsel":
            df.drop(x, inplace=True)

    df['sales'] = pd.Series(df['price'].str[1:]).astype(float) * df['quantity'].astype(int)

    df.drop("price", axis=1, inplace=True)
    df.drop("quantity", axis=1, inplace=True)
    df.drop("product", axis=1, inplace=True)

    return df


filepaths = ["./data/" + f for f in os.listdir("./data/") if f.endswith('.csv')]

df = pd.concat(map(readCSV, filepaths))

df.to_csv('formatted_data.csv', index=False)

print(df)
