import csv

with open('data/daily_sales_data_2.csv', newline='') as file:
    reader = csv.reader(file)  # default delimiter is comma
    with open('pink_morsels_2.csv','w',newline="") as infile:
        writer=csv.writer(infile)
        for row in reader:
            if row[0].strip().lower() == "pink morsel":
                price=float(row[1][1:])
                qunatity=int(row[2])
                val=price*qunatity
                row.append(val)
                writer.writerow(row)
