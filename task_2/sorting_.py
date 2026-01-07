import csv
from datetime import datetime

with open('../task_1/final_data.csv', newline='') as file:
    reader = csv.reader(file)  # default delimiter is comma
    rows=list(reader)

data=rows[:]

data.sort(key=lambda row: datetime.strptime(row[1], '%Y-%m-%d'))

with open('sorted_data.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data)

