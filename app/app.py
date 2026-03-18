import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback

# Load processed data and ensure date is datetime
df = pd.read_csv('../data/daily_sales_data_1.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Initialize Dash app
app = Dash(__name__)

# App layout with header and graph
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Analysis", 
            style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Div([
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': r, 'value': r} for r in sorted(df['Region'].unique())],
            value=df['Region'].unique().tolist(),  # All regions selected by default
            multi=True,
            placeholder="Select regions (Ctrl+click for multiple)",
            style={'width': '50%', 'margin': 'auto'}
        )
    ], style={'padding': '20px'}),
    
    dcc.Graph(id='sales-line-chart')
])

# Callback to update chart based on region selection
@callback(
    Output('sales-line-chart', 'figure'),
    Input('region-dropdown', 'value')
)
def update_chart(selected_regions):
    filtered_df = df[df['Region'].isin(selected_regions)]
    
    fig = px.line(filtered_df, 
                  x='Date', 
                  y='Sales', 
                  color='Region',
                  title="Pink Morsel Sales: Before & After 15 Jan 2021 Price Increase",
                  labels={'Sales': 'Total Sales (£)', 'Date': 'Date'},
                  markers=True)
    
    fig.add_vline(x=pd.to_datetime('2021-01-15'), 
                  line_dash="dash", 
                  line_color="red", 
                  annotation_text="Price Increase")
    
    fig.update_layout(hovermode='x unified', height=600)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
