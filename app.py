import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "formatted_output.csv"

df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])

cutoff = pd.Timestamp("2021-01-15")
REGION_OPTIONS = ["all", "north", "east", "south", "west"]


def create_region_sales_figure(region: str):
    filtered_df = df if region == "all" else df[df["Region"] == region]
    daily = filtered_df.groupby("Date", as_index=False)["Sales"].sum().sort_values("Date")

    fig = px.line(daily, x="Date", y="Sales")
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Sales")
    fig.add_vline(x=cutoff, line_dash="dash", line_color="red")
    return fig

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Pink Morsel Sales"),
        dcc.RadioItems(
            id="region-filter",
            options=[{"label": region, "value": region} for region in REGION_OPTIONS],
            value="all",
            inline=True,
        ),
        dcc.Graph(id="sales-chart", figure=create_region_sales_figure("all")),
    ]
)


@app.callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_region_sales_chart(selected_region: str):
    return create_region_sales_figure(selected_region)


if __name__ == "__main__":
    app.run(debug=True)