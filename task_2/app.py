from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load CSV
df = pd.read_csv('../task_2/sorted_data.csv', header=None, names=['sales', 'date', 'region'])
df['date'] = pd.to_datetime(df['date'])

# Line chart
fig = px.line(
    df,
    x='date',
    y='sales',
    color='region',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Sales'}
)

# Fixed: add vertical line as datetime
vline_date = pd.to_datetime('2021-01-15')
fig.add_vline(
    x=vline_date,
    line_dash="dash",
    line_color="red",
   
)

# Dash app
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
