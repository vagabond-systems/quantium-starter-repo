import csv

with open('pink_morsels_2.csv', newline='') as file:
    reader = csv.reader(file)  # default delimiter is comma
    with open('final_data.csv','a',newline="") as outfile:
        writer=csv.writer(outfile)
        for row in reader:
            sales=row[5]
            date=row[3]
            region=row[4]
            writer.writerow([sales, date, region])

