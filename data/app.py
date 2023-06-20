import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Creating a line chart using dash to display our final data
df = pd.read_csv('concat_file.csv')
df = df.sort_values(by="date")

app = dash.Dash(__name__)

figure = px.line(df, x="date", y="sales", title="Sales Data")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),

    dcc.Graph(
        id='sales-chart',
        figure=figure
    )
])




if __name__ == '__main__':
    app.run_server(debug=False)
