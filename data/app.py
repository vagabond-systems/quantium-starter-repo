import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Ensure correct data types
df["date"] = pd.to_datetime(df["date"])

# 🔥 FIX: make sure sales is numeric (prevents your error)
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Drop any broken rows
df = df.dropna(subset=["sales"])


# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f4f4",
        "padding": "20px"
    },
    children=[

        # Header
        html.H1(
            "Soul Foods Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "white",
                "backgroundColor": "#2c3e50",
                "padding": "15px",
                "borderRadius": "10px"
            }
        ),

        # Radio buttons
        html.Div(
            style={"textAlign": "center", "marginTop": "20px"},
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "backgroundColor": "white",
                        "padding": "10px",
                        "borderRadius": "10px",
                        "display": "inline-block"
                    }
                )
            ]
        ),

        # Graph container
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "marginTop": "20px",
                "borderRadius": "10px",
                "boxShadow": "0px 2px 8px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)


# Callback for updating chart
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    daily_sales = filtered_df.groupby("date")["sales"].sum().reset_index()

    # Create line chart
    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title="Total Daily Sales of Pink Morsels"
    )

    # Add price increase marker
    # Add vertical line (no annotation here)
    fig.add_vline(
        x=pd.to_datetime("2021-01-15"),
        line_dash="dash",
        line_color="red"
    )

    # Add annotation separately
    fig.add_annotation(
        x=pd.to_datetime("2021-01-15"),
        y=daily_sales["sales"].max(),
        text="Price Increase",
        showarrow=True,
        arrowhead=1
    )

    # Labels + styling
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white"
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)