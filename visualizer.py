import pandas as pd
from dash import Dash
from dash import dcc
from dash import html

# Load data
df = pd.read_csv('final.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date') 

# Initialize the Dash app 
app = Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    # Header
    html.H1(children='Soul Foods Sales Visualization'),

    # Line Chart
    dcc.Graph(
        id='sales-chart',
        figure={
            'data': [
                dict(
                    x=df['Date'],
                    y=df['Sales'],
                    mode='lines',
                    name='Sales'
                )
            ],
            'layout': dict(
                title='Sales over time',
                xaxis=dict(title='Date'),
                yaxis=dict(title='Sales'),
                showlegend=True
            )
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
