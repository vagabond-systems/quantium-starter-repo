import datetime
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import glob

app = Dash(__name__)

sales = glob.glob("output_files/pink morsel_sales.csv")

df = pd.read_csv(sales[0], parse_dates=['date'])

df['sales'] = pd.to_numeric(df['sales'].str.replace("$", ""))
df_weekly_sales = (df
    .groupby(
        [pd.Grouper(key="date", freq="7D"), 'region']
    )
    .agg({'sales': 'sum'})
    .reset_index()
)

fig = px.line(
    df_weekly_sales, 
    x="date", 
    y="sales", 
    color="region",
    title="Sales Data around Pink Morsel Price Increase",
    labels={
        "date": "Date",
        "sales": "Sales ($)",
        "region": "Region"
    }
)

fig.add_vline(
    x=datetime.datetime.strptime("2021-01-01", "%Y-%m-%d").timestamp() * 1000, 
    line_dash="dot", 
    line_color="black", 
    annotation_text="Price Increase", 
    annotation_position="top left"
)

app.layout = html.Div(
    title="Sales Data around Pink Morsel Price Increase",
    children=[
        dcc.Graph(
            id="pink-morsel-sales-data",
            figure=fig,
            config={"edits": {"titleText": True}}
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
