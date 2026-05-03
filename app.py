import pandas as pd
from datetime import datetime

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


def load_and_prepare(path='data/processed_sales_data.csv'):
    df = pd.read_csv(path)
    # ensure date column is parsed and sorted
    df['date'] = pd.to_datetime(df['date'])
    # normalize region and product columns
    if 'region' in df.columns:
        df['region'] = df['region'].astype(str).str.strip().str.lower()
    else:
        df['region'] = ''
    return df


def create_app(df):
    app = Dash(__name__)

    # layout with radio items for region filter
    app.layout = html.Div([
        html.Div([
            html.H1('Soul Foods — Pink Morsel Sales Visualiser', className='title'),
            html.P('Use the controls to filter sales by region. The vertical red line marks the price increase on 2021-01-15.', className='subtitle')
        ], className='header'),

        html.Div([
            html.Div([
                html.Label('Select region:', className='control-label'),
                dcc.RadioItems(
                    id='region-radio',
                    options=[
                        {'label': 'All', 'value': 'all'},
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'},
                    ],
                    value='all',
                    labelStyle={'display': 'inline-block'},
                    className='radio'
                )
            ], className='controls'),

            html.Div([
                dcc.Graph(id='sales-graph')
            ], className='chart')
        ], className='content')
    ], className='container')


    def make_figure(selected_region):
        if selected_region is None or selected_region == 'all':
            filtered = df.copy()
            title_suffix = ' (all regions)'
        else:
            filtered = df[df['region'] == selected_region]
            title_suffix = f' ({selected_region})'

        agg = filtered.groupby('date', as_index=False)['sales'].sum().sort_values('date')

        fig = px.line(agg, x='date', y='sales', title='Daily sales for Pink Morsel' + title_suffix)
        fig.update_layout(xaxis_title='Date', yaxis_title='Total sales (AUD)')

        # add a vertical line for the price increase date (use string)
        price_increase = '2021-01-15'
        fig.add_vline(x=price_increase, line_dash='dash', line_color='red')

        try:
            ymax = agg['sales'].max()
        except Exception:
            ymax = None
        if ymax is not None:
            fig.add_annotation(x=price_increase, y=ymax, text='Price increase: 2021-01-15', showarrow=False, yanchor='bottom')
        else:
            fig.add_annotation(x=price_increase, yref='paper', y=1.0, text='Price increase: 2021-01-15', showarrow=False, yanchor='bottom')

        return fig


    @app.callback(Output('sales-graph', 'figure'), [Input('region-radio', 'value')])
    def update_figure(region_value):
        # region_value will be one of 'all','north','east','south','west'
        return make_figure(region_value)

    # set initial figure
    app._initial_figure = make_figure('all')

    return app


if __name__ == '__main__':
    df = load_and_prepare()
    app = create_app(df)
    # default Dash dev server
    app.run(debug=True)
