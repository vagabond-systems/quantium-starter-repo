import csv

# Get the paths to the CSV files
csv_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

# Create a new CSV file to store the combined data
output_file = open("data/combined_sales_data.csv", "w")

# Write the header row to the output file
header = ["Sales", "Date", "Region"]
writer = csv.writer(output_file)
writer.writerow(header)

# Iterate over the CSV files
for csv_file in csv_files:
    # Open the CSV file
    with open(csv_file, "r") as f:
        reader = csv.reader(f)

        # Iterate over the rows in the CSV file
        for row in reader:
            # Check if the product is Pink Morsels
            if row[0] == "pink morsel":
                # Convert the quantity and price fields to integers
                quantity = int(row[1].replace("$", "").replace(".", ""))
                price = int(row[2])

                # Calculate the sales
                sales = (quantity * price)/100

                # Write the row to the output file
                writer.writerow([sales, row[3], row[4]])

# Close the output file
output_file.close()
