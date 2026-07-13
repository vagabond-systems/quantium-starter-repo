import csv
import glob

output_data = []

# Read all CSV files from the data folder
for file in glob.glob("data/*.csv"):
    with open(file, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["product"] == "Pink Morsels":
                sales = float(row["quantity"]) * float(row["price"])

                output_data.append({
                    "Sales": sales,
                    "Date": row["date"],
                    "Region": row["region"]
                })

# Write the output file
with open("formatted_output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Sales", "Date", "Region"])
    writer.writeheader()
    writer.writerows(output_data)

print("formatted_output.csv created successfully!")
