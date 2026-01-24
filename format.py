import pandas as pd
import warnings
warnings.filterwarnings("ignore")

import re

data1 = pd.read_csv("data/daily_sales_data_0.csv")
data2 = pd.read_csv("data/daily_sales_data_1.csv")
data3 = pd.read_csv("data/daily_sales_data_2.csv")

table = pd.concat([data1, data2, data3], ignore_index=True)

table = table[table['product'] == "pink morsel"]


for i in range(0,len(table)):
    price = table['price'].iloc[i]
    pattern = r'[^.0-9]' 
    table["price"].iloc[i] = re.sub(pattern,"",price)


table["price"] = table["price"].astype(float)
table['sales'] = table['price'] * table['quantity']


output_data = table.iloc[:,[5, 3, 4]]

output_data.to_csv("final_data.csv", index = False)