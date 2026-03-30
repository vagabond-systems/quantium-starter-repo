import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


app = Dash(__name__)

# Layout
app.layout = html.Div(style={
    "backgroundColor": "#f4f6f8",
    "padding": "20px",
    "fontFamily": "Arial"
}, children=[

    html.H1("Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }),

    html.Div([
        html.Label("Select Region:",
                   style={"fontWeight": "bold", "marginRight": "10px"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            inline=True
        )
    ], style={"textAlign": "center", "marginBottom": "30px"}),

    dcc.Graph(id="sales-line-chart")
])



@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Sales Trend Over Time (Before vs After Price Increase)"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f8",
        title_x=0.5
    )

    fig.add_vrect(
    x0=filtered_df["date"].min(),
    x1=pd.to_datetime("2021-01-15"),
    fillcolor="green",
    opacity=0.1,
    line_width=0
    )

    fig.add_vrect(
        x0=pd.to_datetime("2021-01-15"),
        x1=filtered_df["date"].max(),
        fillcolor="red",
        opacity=0.1,
        line_width=0
    )

  
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

    return fig


if __name__ == "__main__":
    app.run(debug=True)