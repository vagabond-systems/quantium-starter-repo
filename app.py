import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read the data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Group sales by date
daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Dashboard"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)