from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import glob

# DATA EXPECTED: product, price, quantity, date, region

# Read and combine all local CSVs with the same schema
files = sorted(glob.glob('data/daily_sales_data_*.csv'))
if files:
    df_list = [pd.read_csv(f) for f in files]
    df = pd.concat(df_list, ignore_index=True)
else:
    # fallback if no files found
    df = pd.DataFrame(columns=['product', 'price', 'quantity', 'date', 'region'])

# dataset0 = pd.read_csv('data/daily_sales_data_0.csv')
# dataset1 = pd.read_csv('data/daily_sales_data_1.csv')
# dataset2 = pd.read_csv('data/daily_sales_data_2.csv')
# options = [datasert0, dataset1, dataset2]
# clickable options for dataset selection - default to dataset0

app = Dash(__name__)
# Minimal data preparation
# ensure date is datetime and numeric columns are numeric
df['date'] = pd.to_datetime(df['date'], errors='coerce')
# clean price: remove any non-digit except dot, then convert to float
df['price'] = df['price'].astype(str).replace(r'[^0-9\.]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

# drop rows missing essential values to avoid expensive/incorrect aggregations
df = df.dropna(subset=['date', 'price', 'quantity'])

# sort by date for nicer plotting
df = df.sort_values('date')

# compute revenue
df['revenue'] = df['price'] * df['quantity']

# top products by quantity
product_agg = (
    df.groupby('product', as_index=False)
      .agg(total_quantity=('quantity', 'sum'), total_revenue=('revenue', 'sum'))
)
product_agg = product_agg.nlargest(10, 'total_quantity')

# KPI values
total_revenue = df['revenue'].sum()
total_units = df['quantity'].sum()
df['price'] = df['price'].replace('[\\$\\,\\.]', '', regex=True).astype(int)
avg_price = df['price'].mean()

# daily aggregation for time series (use full datetime so Plotly handles x-axis correctly)
daily = (
        df.groupby(pd.Grouper(key='date', freq='D'), as_index=False)
            .agg({'quantity': 'sum', 'revenue': 'sum'})
)

# combined time series figure: revenue (left y) and units (right y)
ts_fig = go.Figure()
ts_fig.add_trace(go.Scatter(x=daily['date'], y=daily['revenue'], mode='lines', name='Revenue'))
ts_fig.add_trace(go.Scatter(x=daily['date'], y=daily['quantity'], mode='lines', name='Units', yaxis='y2'))
ts_fig.update_layout(title='Daily Revenue and Units', xaxis_title='date', yaxis=dict(title='revenue'), yaxis2=dict(title='units', overlaying='y', side='right'))

# standalone revenue line chart (styled)
rev_fig = px.line(daily, x='date', y='revenue', title='Daily Revenue', template='plotly_dark')
rev_fig.update_traces(line=dict(width=2))

prod_fig = px.bar(product_agg, x='product', y='total_quantity', title='Top Products by Quantity')

# layout: KPI row + time series + top products
app.layout = html.Div([
    html.H2('Soul Foods — Sales overview'),

    # KPI cards
    html.Div([
        html.Div([html.H4('Total revenue'), html.P(f"${total_revenue:,.2f}")], style={'padding': '10px', 'flex': '1'}),
        html.Div([html.H4('Total units'), html.P(f"{int(total_units):,}")], style={'padding': '10px', 'flex': '1'}),
        html.Div([html.H4('Average price'), html.P(f"${avg_price:,.2f}")], style={'padding': '10px', 'flex': '1'})
    ], style={'display': 'flex', 'gap': '10px'}),

    # time series graphs: combined and standalone revenue (side-by-side)
    html.Div([
        html.Div(dcc.Graph(figure=ts_fig, id='ts-combined'), style={'flex': '1'})
    ], style={'display': 'flex', 'gap': '10px'}),

    # # top products
    # html.Div([
    #     dcc.Graph(figure=prod_fig, id='prod-bar')
    # ])
], style={'margin': '20px'})


if __name__ == '__main__':
    app.run(debug=True)
