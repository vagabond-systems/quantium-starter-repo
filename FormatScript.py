import pandas as pd
import os

def readCSV(path):
    df_i = pd.read_csv(path, delimiter=";", parse_dates=['date'], dayfirst=True)

    df_i = df_i[df_i['product'] == "pink morsel"]

    # Make a new column sales before removing quantity & price & product
    df_i['sales'] = pd.Series(df_i['price'].str[1:]).astype(float) * df_i['quantity'].astype(int)

    df_i.drop("price", axis=1, inplace=True)
    df_i.drop("quantity", axis=1, inplace=True)
    df_i.drop("product", axis=1, inplace=True)

    return df_i

# Merge the 3 csv
filepaths = ["./data/" + f for f in os.listdir("./data/") if f.endswith('.csv')]
df = pd.concat(map(readCSV, filepaths))

# Then write it to a new formated csv
df.to_csv('formatted_data.csv', index=False)

print(df)
