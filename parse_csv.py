import csv
import os
import glob

# Initialize an empty list to store the rows of data
filtered_data = []

 # Specify the fieldnames for the output CSV
fieldnames = ['Sales', 'Date', 'Region']

    

for csv_filename in ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']:
    with open(csv_filename, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)
        
        # Process each row in the CSV file
        for row in csv_reader:
            # If the product is a Pink Morsel...
            if row['product'].lower() == 'pink morsel':
                # Multiply price and quantity (convert price to float and remove $ sign first) 
                sales = float(row['price'].replace("$", "")) * int(row['quantity'])
                
                # Append the formatted row to the list
                filtered_data.append({
                    'Sales': sales,
                    'Date': row['date'],
                    'Region': row['region'],
                })
        # Create a new CSV file for the output data
        with open('final.csv', 'w', newline='') as csv_file:
            # Create a CSV writer
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            
            # Write the header
            csv_writer.writeheader()

            # Write the rows of data
            for row in filtered_data:
                csv_writer.writerow(row)

