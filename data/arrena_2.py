import pandas
import csv


current_file = 'data/daily_sales_data_2.csv'
new_file = 'final_result_2.csv'

with open(current_file, 'r') as file, open(new_file, 'w', newline='') as new:
    reader = csv.DictReader(file)
    writer = csv.writer(new)

    # Write the header row
    writer.writerow(['sales', 'date', 'region'])

    for row in reader:
        product = row['product']
        if product == 'pink morsel':
            price = float(row['price'].replace('$', ''))
            quantity = int(row['quantity'])
            sales = price * quantity
            date = row['date']
            region = row['region']
            writer.writerow([sales, date, region])


file_path = 'final_result_2.csv'

# Read the CSV file into a DataFrame
df = pandas.read_csv(file_path, index_col='sales', parse_dates=['date'])

# Print the contents of the DataFrame
print(df)