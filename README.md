import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the CSV file containing sales data
sales_data = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# Convert 'date' column to datetime
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Sort data by date
sales_data = sales_data.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer"),
    dcc.Graph(id='sales-chart'),
])

# Define callback to update the chart based on user input
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('sales-chart', 'hoverData')]
)
def update_chart(hoverData):
    # Filter data before and after the price increase
    before_increase = sales_data[sales_data['date'] < '2021-01-15']
    after_increase = sales_data[sales_data['date'] >= '2021-01-15']
    
    # Create line chart
    fig = px.line(sales_data, x='date', y='Sales', title="Sales Before and After Pink Morsel Price Increase")
    
    # Highlight the price increase date
    fig.add_vline(x='2021-01-15', line_dash="dash", annotation_text="Price Increase", annotation_position="top right")
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
