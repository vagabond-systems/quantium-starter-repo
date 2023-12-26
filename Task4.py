#!/usr/bin/env python
# coding: utf-8

# In[4]:



from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Your data loading and processing code remains the same...
df_0 = pd.read_csv('daily_sales_data_0.csv')

# Filter rows where 'product' is 'pink morsel'
df_0 = df_0[df_0['product'] == 'pink morsel']

# Convert 'price' column to numeric
df_0['price'] = pd.to_numeric(df_0['price'].str.replace('$', '', regex=False), errors='coerce')

# Calculate 'sales' column
df_0['sales'] = df_0['price'] * df_0['quantity']

# Drop unnecessary columns
columns_to_drop = ['price', 'quantity']
df_0 = df_0.drop(columns=columns_to_drop)

# Print the resulting DataFrame
# print(df_0)

df_1 = pd.read_csv('daily_sales_data_1.csv')

# Filter rows where 'product' is 'pink morsel'
df_1 = df_1[df_1['product'] == 'pink morsel']

# Convert 'price' column to numeric
df_1['price'] = pd.to_numeric(df_1['price'].str.replace('$', '', regex=False), errors='coerce')

# Calculate 'sales' column
df_1['sales'] = df_1['price'] * df_1['quantity']

# Drop unnecessary columns
columns_to_drop = ['price', 'quantity']
df_1 = df_1.drop(columns=columns_to_drop)

# Print the resulting DataFrame
# print(df_1)

df_2 = pd.read_csv('daily_sales_data_2.csv')

# Filter rows where 'product' is 'pink morsel'
df_2 = df_2[df_2['product'] == 'pink morsel']

# Convert 'price' column to numeric
df_2['price'] = pd.to_numeric(df_2['price'].str.replace('$', '', regex=False), errors='coerce')

# Calculate 'sales' column
df_2['sales'] = df_2['price'] * df_2['quantity']

# Drop unnecessary columns
columns_to_drop = ['price', 'quantity']
df_2 = df_2.drop(columns=columns_to_drop)

# Print the resulting DataFrame

combined_df = pd.concat([df_0,df_1,df_2],ignore_index = True)
combined_df = combined_df.drop(columns = 'product')
# add 4 regions sales value here-------
grouped_df = combined_df.groupby('date')['sales'].sum().reset_index()

# Merge the grouped DataFrame back to the original DataFrame based on 'Date'
merged_df = pd.merge(combined_df, grouped_df, on='date',suffixes=('', '_total'))
merged_df = merged_df.drop(columns = 'sales')
merged_df=merged_df.drop_duplicates(subset='date',ignore_index=True)
merged_df['region']='all'

c_north = combined_df[combined_df['region'] == 'north']
c_south = combined_df[combined_df['region'] == 'south']
c_east = combined_df[combined_df['region'] == 'east']
c_west = combined_df[combined_df['region'] == 'west']

sales_on_query_data_north = c_north.loc[c_north['date']== '2021-01-15','sales'] 
north_range=sales_on_query_data_north.values[0]  if not sales_on_query_data_north.empty else 0
line_color = ['sales greater than thresold' if y > north_range else 'sales lesser than thresold' for y in c_north['sales']]
c_north.loc[:, 'Color'] = line_color

sales_on_query_data_south = c_south.loc[c_south['date']== '2021-01-15','sales'] 
south_range=sales_on_query_data_south.values[0]  if not sales_on_query_data_south.empty else 0
line_color = ['sales greater than thresold' if y > south_range else 'sales lesser than thresold' for y in c_south['sales']]
c_south.loc[:, 'Color'] = line_color

sales_on_query_data_east = c_east.loc[c_east['date']== '2021-01-15','sales'] 
east_range=sales_on_query_data_east.values[0]  if not sales_on_query_data_east.empty else 0
line_color = ['sales greater than thresold' if y > east_range else 'sales lesser than thresold' for y in c_east['sales']]
c_east.loc[:, 'Color'] = line_color

sales_on_query_data_west = c_west.loc[c_west['date']== '2021-01-15','sales'] 
west_range=sales_on_query_data_west.values[0]  if not sales_on_query_data_west.empty else 0
line_color = ['sales greater than thresold' if y > west_range else 'sales lesser than thresold' for y in c_west['sales']]
c_west.loc[:, 'Color'] = line_color

sales_on_query_data_all = merged_df.loc[merged_df['date']== '2021-01-15','sales_total'] 
all_range=sales_on_query_data_all.values[0]  if not sales_on_query_data_all.empty else 0
line_color = ['sales greater than thresold' if y > all_range else 'sales lesser than thresold' for y in merged_df['sales_total']]
merged_df.loc[:, 'Color'] = line_color

app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods',
        style={
            'textAlign': 'center'
        }
    ),

    html.Div(children='Sales after Rise in price of Pink Morsel', id="header",style={
        'textAlign': 'center'
    }),

    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All','value':'all'},
        ],
        value='north',  # Default value
        labelStyle={'display': 'block'}
    ),

    dcc.Graph(
        id='line-chart',
    )
])

# Callback to update the line chart based on the selected region
@app.callback(
    Output('line-chart', 'figure'),
    [Input('region-selector', 'value')]
)

def update_line_chart(selected_region):
    if selected_region == 'all':
        fig = px.line(merged_df, x='date', y='sales_total', color='Color', title='Sales in all regions(threshold = sales on Jan 15, 2021)')
    else:
        region_data = None
        if selected_region == 'north':
            region_data = c_north
        elif selected_region == 'south':
            region_data = c_south
        elif selected_region == 'east':
            region_data = c_east
        elif selected_region == 'west':
            region_data = c_west

        fig = px.line(region_data, x='date', y='sales', color='Color', title=f'Sales in {selected_region} region(threshold = sales on Jan 15, 2021)')

    return fig

if __name__ == '__main__':
    app.run(debug=True,port=8052)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




