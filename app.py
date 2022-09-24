from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_data.csv", parse_dates=['date'], dayfirst=True)
df['date']= df['date'].dt.to_period('M')
df = df.groupby([df['date'].astype(str), 'region'])['sales'].sum()

app = Dash(__name__)
fig = px.line(df, x= df.index.get_level_values(0), y = 'sales',  color = df.index.get_level_values(1))
app.layout = html.Div([
    dcc.Graph(id='Sales', figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)