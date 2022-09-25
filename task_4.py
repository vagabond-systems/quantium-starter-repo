from dash import Dash,html,dcc,Input, Output
import plotly.express as px
from plotly.express import line
import pandas as pd

data=pd.read_csv('./data/ouput.csv')
data.sort_values(by="date")

app=Dash(__name__)

def generate_graph(data):
    lineChart=line(data,x='date',y='sale',title='pink morsel sale\'s')
    return lineChart

graph=dcc.Graph(id='graph',figure=generate_graph(data))
header=html.H1(id='header',children=["Pink Morsel Visualizer"])
regionPick=dcc.RadioItems(["north", "east", "south", "west", "all"],"north",id="regionPick")
regionWrap=html.Div([regionPick])

@app.callback(
    Output(graph,'figure'),
    Input(regionPick,'value')
    )

def updateGraph(region):
    if region=='all':
        udata=data
    else:
        udata=data[data['region']==region]
    fig=generate_graph(udata)
    return fig

app.layout=html.Div([
    header,
    graph,
    regionWrap])
    


app.run_server()
