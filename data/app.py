import pandas as pd
import dash
from dash import html, dcc

# Creating a line chart using dash to display our final data
df = pd.read_csv('concat_file.csv')

app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1('Sales comparison for pink morsel', style={'textAlign': 'center', 'color': '#7FDBFF'}),
        dcc.Graph(
            id='sales-chart',
            figure={
                'data': [
                    {'x': df['date'], 'y': df['sales'], 'type': 'line'},
                ],
                'layout': {
                    'title': 'Sales Data',
                    'xaxis': {'title': 'date'},
                    'yaxis': {'title': 'sales'},
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
