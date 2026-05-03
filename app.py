import pandas as pd
from datetime import datetime

from dash import Dash, dcc, html
import plotly.express as px


def load_and_prepare(path='data/processed_sales_data.csv'):
    df = pd.read_csv(path)
    # ensure date column is parsed and sorted
    df['date'] = pd.to_datetime(df['date'])
    # aggregate total sales per date (sum across regions)
    agg = df.groupby('date', as_index=False)['sales'].sum()
    agg = agg.sort_values('date')
    return agg


def create_app(df):
    app = Dash(__name__)

    fig = px.line(df, x='date', y='sales', title='Daily sales for Pink Morsel')
    fig.update_layout(xaxis_title='Date', yaxis_title='Total sales (AUD)')

    # add a vertical line for the price increase date (use string to avoid dtype mixing)
    price_increase = '2021-01-15'
    fig.add_vline(x=price_increase, line_dash='dash', line_color='red')

    # place a separate annotation at the top of the chart
    try:
        ymax = df['sales'].max()
    except Exception:
        ymax = None
    if ymax is not None:
        fig.add_annotation(x=price_increase, y=ymax, text='Price increase: 2021-01-15', showarrow=False, yanchor='bottom')
    else:
        fig.add_annotation(x=price_increase, yref='paper', y=1.0, text='Price increase: 2021-01-15', showarrow=False, yanchor='bottom')

    app.layout = html.Div([
        html.H1('Soul Foods — Pink Morsel Sales Visualiser'),
        html.P('This graph answers: Were sales higher before or after the Pink Morsel price increase on 15 Jan 2021?'),
        dcc.Graph(figure=fig),
    ], style={'maxWidth': '900px', 'margin': 'auto', 'fontFamily': 'Arial'})

    return app


if __name__ == '__main__':
    df = load_and_prepare()
    app = create_app(df)
    # default Dash dev server
    app.run(debug=True)
