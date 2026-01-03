import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Data load karein
df = pd.read_csv('final_processed_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Daily total revenue calculate karein
daily_revenue = df.groupby('date')['revenue'].sum().reset_index()
fig = px.line(daily_revenue, x='date', y='revenue', title='Sales Performance')
fig.update_traces(line_color='#FF69B4') # Pink color theme
#layout
app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f2f2f2', 'padding': '20px'}, children=[
    html.H1("Pink Morsels Dashboard", style={'textAlign': 'center', 'color': '#FF69B4'}),

    html.Div(style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px'}, children=[
        dcc.Graph(id='sales-graph', figure=fig)
    ])
])

if __name__ == '__main__':
    app.run(debug=True)