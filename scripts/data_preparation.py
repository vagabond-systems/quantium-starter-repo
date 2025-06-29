import csv
import os
import pandas as pd

print("Before:",os.getcwd()) #check current directory
os.chdir(r'C:\Users\Sia\Documents\quantium_tech_interview\quantium-starter-repo\data') #move to where files are
print("After:",os.getcwd()) #check the changed directory
print("Files in directory:", os.listdir())

#import csv files as dataframes into a list
data_sets = []
for file in os.listdir():
    if file.endswith('.csv'):
        file = pd.read_csv(file)
        data_sets.append(file)


#remove rows that are not pink morsels
#merge quantity and price by times to create a new column sales
#then remove product as not necessary

processed_datasets = []

def processing_datasets(datasets):
    for i in datasets:
        i['price'] = i['price'].str.replace('$', '')
        i['price'] = pd.to_numeric(i['price'], errors='coerce')
        i['sales'] = i['price'] * i['quantity']
        i = i[i['product'].str.contains('pink morsel', na=False)]
        i = i[['sales', 'date', 'region']]
        processed_datasets.append(i)
    return processed_datasets

processing_datasets(data_sets)
pd.concat(processed_datasets, ignore_index = True).to_csv('processed_data.csv')

