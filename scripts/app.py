# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import os
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from datetime import datetime


app = Dash()
os.chdir(r'C:\Users\Sia\Documents\quantium_tech_interview\quantium-starter-repo\data')
processed_data =pd.read_csv('processed_data.csv', parse_dates=['date'])


fig = px.line(processed_data, x="date", y="sales", title = "Sales over Time" )

# Add vertical line at 15th Jan 2021
fig.add_vline(
    x=datetime(2021, 1, 15),
    line_dash="dash",
    line_color="red",
)
fig.update_layout(
    xaxis=dict(
        title = "Time"
    ),
    yaxis=dict(
        title = "Sales ($)"
    )
)

app.layout = html.Div(children=[
    html.H1(children='Data Visualisation'),

    html.Div(children='''
        Visualisation of sales data of "Pink Morsel" over the years.
        The red vertical line indicates the time when price for "Pink Morsel was increased." 
    '''),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
     app.run(debug=True)
