import datetime
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import glob

from plotly import graph_objects as go
from typing import List

app = Dash(__name__)


PRODUCT_NAME = "pink morsel"
FILE_NAME = f"output_files/{PRODUCT_NAME}_sales.csv"
REGIONS: List[str] = ["North", "South", "East", "West"]


# Helper functions
def parse_data_file(FILE_NAME: str) -> pd.DataFrame:
    data = glob.glob(FILE_NAME)
    df = pd.read_csv(data[0], parse_dates=['date'])
    df["sales"] = pd.to_numeric(df['sales'].str.replace("$", ""))
    df["region"] = df["region"].str.capitalize()
    return df


def styled_line_figure(df: pd.DataFrame, title: str) -> go.Figure:
    fig = px.line(
        data_frame=df,
        x="date", 
        y="sales", 
        title=title,
        labels={
            "date": "Date",
            "sales": "Sales ($)",
        },
    )
    fig.add_vline(
        x=datetime.datetime.strptime("2021-01-01", "%Y-%m-%d").timestamp() * 1000, 
        line_dash="dot", 
        line_color="black",
        annotation_text="Price Increase", 
        fillcolor="black",
        annotation_position="top"
    )
    fig.update_traces(line=dict(width=2, color='Fuchsia'))
    fig.update_layout(
        title_font_size=24,
        title_x=0.5,
        paper_bgcolor='RoyalBlue', 
        font=dict(color="white")
    )
    return fig


# Figure initialisation
df = parse_data_file(FILE_NAME)
df_weekly_sales = (df
    .groupby(
        [pd.Grouper(key="date", freq="10D"), 'region']
    )
    .agg({'sales': 'sum'})
    .reset_index()
)

fig = styled_line_figure(df_weekly_sales, "pink morsel")


# Radio callback
@app.callback(
    Output("ProductSalesGraph", "figure"),
    Input("RadioButton", 'value'),
)
def update_graph(region: str, df: pd.DataFrame = df_weekly_sales) -> go.Figure:
    if region and region in REGIONS:
        df = df[df["region"].str.lower() == region.lower()]

    return styled_line_figure(
        df=df,
        title=f"Sales Data for {PRODUCT_NAME.title()}s"
    )


# Styling
centred_div = {
    "justify-content": "center",
    "display": "flex",
    "font-family": "Open Sans, verdana, arial, sans-serif"
}

radio_button = {
    "margin-top": "10px",
    "padding": "5px",
    "border-radius": "5px",
    "color": "white",
    "background-color": "RoyalBlue",
}

# App Layout
app.layout = html.Div(
    title="Sales Data around Pink Morsel Price Increase",
    children=[
        html.H1(
            "Sales Data from Pink Morsel Price Increase",
            id="Header"
        ),
        dcc.Graph(
            figure=fig,
            id="ProductSalesGraph",
            config={"edits": {"titleText": True}}
        ),
        html.Div(
            style=centred_div,
            children=[
                dcc.RadioItems(
                    id="RadioButton",
                    style=radio_button,
                    options=(
                        [{"label": "All", "value": "All"}] + 
                        [{"label": r, "value": r} for r in REGIONS]
                    ),
                    inline=True
                )
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
