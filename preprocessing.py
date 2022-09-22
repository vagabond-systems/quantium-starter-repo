import pandas as pd
import os

def preProcess(name,opFile):
    data=pd.read_csv(name)
    data=data.loc[data['product']=='pink morsel']
    data['price']=data['price'].str.replace(r'$','',regex=True)
    data['sale']=data['price'].astype(float)*data['quantity'].astype(int)
    data=data.sort_values('region')
    data=data.drop(['product','price','quantity'],axis=1)
    return data

output=pd.DataFrame()
for i in os.listdir('./data'):
    output=pd.concat([output,preProcess('./data/'+i,output)])
    
    
output.to_csv('./data/ouput.csv')
