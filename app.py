import pandas as pd
import datetime
import dash
from dash import html, dcc, Input, Output
import plotly.express as px

# === Load and prepare data ===
df = pd.read_csv("processed_data/pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Aggregate weekly sales
df = (
    df.groupby([pd.Grouper(key="date", freq="W"), "region"])["sales"]
    .sum()
    .reset_index()
)

# === Initialize Dash app ===
app = dash.Dash(__name__)

app.title = "Pink Morsel Sales Dashboard"

# === App Layout ===
app.layout = html.Div(
    style={
        "backgroundColor": "#121212",
        "fontFamily": "Arial, sans-serif",
        "color": "#EAEAEA",
        "padding": "30px",
    },
    children=[
        html.H1(
            "Soul Foods: Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#FF66B2"},
        ),

        html.Div(
            [
                html.Label(
                    "Select Region:",
                    style={"fontSize": "18px", "marginRight": "15px"},
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "6px", "marginLeft": "15px"},
                    labelStyle={"fontSize": "16px"},
                    style={"textAlign": "center", "marginBottom": "20px"},
                ),
            ]
        ),

        dcc.Graph(id="sales-graph", style={"height": "600px"}),
    ],
)

# === Callback for interactivity ===
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Build chart
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region" if selected_region == "all" else None,
        title=f"Pink Morsel Weekly Sales ({selected_region.capitalize()})",
        labels={"date": "Date", "sales": "Total Weekly Sales ($)", "region": "Region"},
        template="plotly_dark",
    )

    # Add price increase marker
    price_increase_date = datetime.datetime(2021, 1, 15)
    fig.add_vline(
        x=price_increase_date,
        line_width=3,
        line_dash="dash",
        line_color="#FF3366",
    )
    fig.add_annotation(
        x=price_increase_date,
        y=filtered_df["sales"].max() if not filtered_df.empty else 0,
        text="Price Increase (15 Jan 2021)",
        showarrow=True,
        arrowhead=2,
        ax=50,
        ay=-40,
        font=dict(size=12, color="#FF3366"),
    )

    # Improve layout
    fig.update_layout(
        title_x=0.5,
        hovermode="x unified",
        font=dict(size=14),
        legend_title_text="Region",
        margin=dict(l=40, r=40, t=80, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    return fig


# === Run server ===
if __name__ == "__main__":
    app.run(debug=True)
