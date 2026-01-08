import csv

# Define the source files and the final destination
folder_path = "data/"
input_files = [
    f"{folder_path}daily_sales_data_0.csv",
    f"{folder_path}daily_sales_data_1.csv",
    f"{folder_path}daily_sales_data_2.csv"
]
output_file = "formatted_data.csv"

# This list will store our processed rows before we write them to the new file
final_data_list = []

# 1. Loop through each file path in our list
for file_path in input_files:
    with open(file_path, mode='r') as csv_file:
        # DictReader allows us to access columns by their header names
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            # 2. Filter for Pink Morsels only
            if row['product'] == "pink morsel":
                
                # 3. Calculate Sales (Price * Quantity)
                # We strip the '$' and convert to float/int for math
                price = float(row['price'].replace('$', ''))
                quantity = int(row['quantity'])
                sales = price * quantity
                
                # 4. Create a clean dictionary with only the requested fields
                clean_row = {
                    "sales": sales,
                    "date": row['date'],
                    "region": row['region']
                }
                final_data_list.append(clean_row)

# 5. Write the accumulated data to your output file
with open(output_file, mode='w', newline='') as output_csv:
    headers = ["sales", "date", "region"]
    writer = csv.DictWriter(output_csv, fieldnames=headers)
    
    writer.writeheader()
    writer.writerows(final_data_list)

print(f"Done! {len(final_data_list)} rows processed into {output_file}")