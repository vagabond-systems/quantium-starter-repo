import pandas as pd

# Read CSV files
df1 = pd.read_csv('data/file1.csv')
df2 = pd.read_csv('data/file2.csv')
df3 = pd.read_csv('data/file3.csv')

# Filter rows by product
df1 = df1[df1['product'] == 'Pink Morsels']
df2 = df2[df2['product'] == 'Pink Morsels']
df3 = df3[df3['product'] == 'Pink Morsels']

# Create 'Sales' column
df1['Sales'] = df1['quantity'] * df1['price']
df2['Sales'] = df2['quantity'] * df2['price']
df3['Sales'] = df3['quantity'] * df3['price']

# Keep only required columns
df1 = df1[['Sales', 'date', 'region']]
df2 = df2[['Sales', 'date', 'region']]
df3 = df3[['Sales', 'date', 'region']]

# Concatenate DataFrames
result = pd.concat([df1, df2, df3])

# Write to output CSV file
result.to_csv('output.csv', index=False)
