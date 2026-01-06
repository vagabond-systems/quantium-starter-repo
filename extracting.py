import csv

with open('data/daily_sales_data_0.csv', newline='') as file:
    reader = csv.reader(file)  # default delimiter is comma
    with open('pink_morsels_0.csv','w',newline="") as infile:
        writer=csv.writer(infile)
        for row in reader:
            if row[0].strip().lower() == "pink morsel":
                writer.writerow(row)

