
import pandas as pd

df1= pd.read_csv('data\daily_sales_data_0.csv')
df2= pd.read_csv('data\daily_sales_data_1.csv')
df3 = pd.read_csv('data\daily_sales_data_2.csv')
# Combine the two dataframes
# print(df1.head())
# print(df2.head())
# print(df3.head())
combined_df = pd.concat([df1, df2, df3], ignore_index=True)
print(combined_df.head())

