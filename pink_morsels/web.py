from pathlib import Path
from dash import Dash, html, dcc, Input, Output
from .data import load_data, daily_sales_by_region
from .viz import make_figure


def create_app():
    # Ensure Dash knows where the project's `assets/` folder is.
    assets_path = str(Path(__file__).resolve().parents[1] / 'assets')
    app = Dash(__name__, assets_folder=assets_path)

    # load raw data once and reuse in callbacks
    df_raw = load_data()

    # initial aggregated data for 'all' regions
    initial = daily_sales_by_region(df_raw, 'all')
    fig = make_figure(initial)

    app.layout = html.Div(children=[
        html.Div([
            html.H1("Pink Morsels Sales Visualiser"),
            html.P("Were sales higher before or after the price increase on 2021-01-15?"),
        ], id='header'),

        html.Div([
            dcc.RadioItems(
                id='region-picker',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                ],
                value='all',
                inline=True,
                inputStyle={'margin-right': '6px', 'margin-left': '12px'},
                # add a stable hook class so CSS can target this component
                className='region-radio',
                # move per-label visual styling into the component props where possible
                labelStyle={
                    'background': '#eef4ff',
                    'padding': '6px 10px',
                    'borderRadius': '6px',
                    'marginRight': '8px',
                    'display': 'inline-block'
                }
            )
        ], id='controls'),

        dcc.Graph(id='sales-graph', figure=fig)
    ],
        id='main-container',
        style={'width': '90%', 'maxWidth': '1000px', 'margin': 'auto', 'fontFamily': 'Arial'})


    @app.callback(Output('sales-graph', 'figure'), Input('region-picker', 'value'))
    def update_figure(region_value):
        daily = daily_sales_by_region(df_raw, region_value)
        return make_figure(daily)

    return app
