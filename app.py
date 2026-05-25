import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the processed data
df = pd.read_csv("data/output.csv")

# Sort by date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create the Dash app
app = dash.Dash(__name__)

# Create the line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)", "region": "Region"}
)

# Add vertical line for price increase on Jan 15, 2021
price_increase_date = pd.Timestamp("2021-01-15").timestamp() * 1000
fig.add_vline(
    x=price_increase_date,
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase"
)

# App layout
app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)