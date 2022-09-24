from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

DATA_PATH = "./formatted_data.csv"
COLORS = {
    "primary": "#31C6D4",
    "secondary": "#FF1E1E",
    "font": "#522A61"
}

df = pd.read_csv(DATA_PATH, parse_dates=['date'], dayfirst=True)
df['date'] = df['date'].dt.to_period('M')
df = df.groupby([df['date'].astype(str), 'region'])['sales'].sum()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Visualizer", style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px" }),

    dcc.Graph(id='SalesGraph'),

    html.Div(dcc.RadioItems(['all', 'north', 'south', 'east', 'west'], 'all', id='RadioItem', inline=True),
             style = {"font-size": "150%"})

], style={'width': '100%',"textAlign": "center",
        'display': 'inline-block', "background-color": COLORS["primary"],
        "border-radius": "20px"})


@app.callback(
    Output('SalesGraph', 'figure'),
    Input('RadioItem', 'value')
)
def update_graph(radio_item):
    if radio_item == 'all':
        dff = df
    else:
        dff = df[df.index.get_level_values('region').isin([radio_item])]

    fig = px.line(dff, x=dff.index.get_level_values(0), y='sales', color=dff.index.get_level_values('region'))
    fig.update_xaxes(title='Date')
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
