import pandas as pd
import dash
from dash import html, dcc, callback
import plotly.express as px

# Creating a line chart using Dash to display our final data
df = pd.read_csv('concat_file.csv')
df = df.sort_values(by="date")

app = dash.Dash(__name__)

color = {
    'background': 'black'
}

available_regions = ['north', 'south', 'east', 'west', 'all']

figure = px.line(df, x="date", y="sales", title="sales-chart")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales', style={'textAlign': 'center', 'color': '#7FDBFF', 'font-weight': 'bold'}),

    html.Div(
        id='header',
        children=[
            html.Label('Filter by Region:', style={'font-weight': 'bold', 'margin-right': '10px', 'color': 'green'}),
            dcc.RadioItems(
                id='region-button',
                options=[{'label': region, 'value': region} for region in available_regions],
                value='all',
                labelStyle={'display': 'inline-block', 'margin-right': '10px', 'background': 'black', 'color': 'yellow'}
            ),
            html.Div(id='sales-chart-container', children=[
                dcc.Graph(
                    id='sales-chart',
                    figure=figure
                )
            ])
        ]
    )
])


@app.callback(
    dash.dependencies.Output('sales-chart', 'figure'),
    [dash.dependencies.Input('region-button', 'value')]
)
def update_chart(region):
    if region == 'all':
        filtered_df = df
        title = 'Total Sales - All Regions'
    else:
        filtered_df = df[df['region'] == region]
        title = f'Total Sales - {region.capitalize()} Region'
    
    figure = px.line(filtered_df, x="date", y="sales", title=title)
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)