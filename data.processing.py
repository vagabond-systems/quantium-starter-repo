import pandas as pd 
import os 

def process_data():
    df_0 = pd.read_csv('data/daily_sales_data_0.csv')
    df_1 = pd.read_csv('data/daily_sales_data_1.csv')
    df_2 = pd.read_csv('data/daily_sales_data_2.csv')

    combined_df = pd.concat([df_0, df_1, df_2])

    # 3. Filter for Pink Morsels
    pink_morsels_df = combined_df[combined_df['product'].str.lower() == 'pink morsel'].copy()

    pink_morsels_df['price'] = pink_morsels_df['price'].replace('[\$,]', '', regex=True).astype(float)
    pink_morsels_df['sales'] = pink_morsels_df['price'] * pink_morsels_df['quantity']


    final_df = pink_morsels_df[['sales', 'date', 'region']]

    final_df.to_csv('formatted_data.csv', index=False)
    print("Success! formatted_data.csv has been created.")

if __name__ == "__main__":
    process_data()