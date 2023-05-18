import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read the formatted sales data from the CSV file
df = pd.read_csv('data/combined_sales_data.csv')

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(
    children=[
        html.H1("Sales Data Visualization"),
        dcc.Graph(
            id='sales-chart',
            figure=px.line(df, x='Date', y='Sales', title='Sales Data')
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
