
from calendar import month

import pandas as pd

df1= pd.read_csv('data\daily_sales_data_0.csv')
df2= pd.read_csv('data\daily_sales_data_1.csv')
df3 = pd.read_csv('data\daily_sales_data_2.csv')
# Combine the two dataframes
# print(df1.head())
# print(df2.head())
# print(df3.head())
combined_df = pd.concat([df1, df2, df3], ignore_index=True)
# print(combined_df.head())
# print(combined_df.columns)
# print(combined_df.info())
# print(combined_df['price'])
# print("/n")

def clean(df):
    df = df.dropna()  # Remove rows with missing values
    # Convert to datetime safely
    for col in ['product']:
        #if product is not pink morsel then drop
        df = df[df['product'] == 'pink morsel']

    for col in ['price']:
        df[col] = df[col].str.replace('$', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['sales'] = df['quantity'] * df['price'].astype(float)

    # Extract components
    for col in ['date']:
        df[col] = pd.to_datetime(df[col], errors='coerce')

        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day

    return df

cleaned_df = clean(combined_df)
# print(cleaned_df.shape[0])
# print(cleaned_df.head())

# # sales per year
# sales_per_year = cleaned_df.groupby('year')['sales'].sum()
# print(sales_per_year)

# # sales before january 15th, 2021
# sales_before_jan15_2021 = cleaned_df[cleaned_df['date'] < '2021-01-15']['sales'].sum()
# print(sales_before_jan15_2021)
# # sales after january 15th, 2021
# sales_after_jan15_2021 = cleaned_df[cleaned_df['date'] > '2021-01-15']['sales'].sum()
# print(sales_after_jan15_2021)

# print(cleaned_df['sales'])

final_df = cleaned_df[['date', 'year','month','day', 'sales', 'region']]
print(final_df.head())

#write to csv
final_df.to_csv('cleaned_sales_data.csv', index=False)
