import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv(r"D:\Python\Quantium\quantium-starter-repo-main\quantium-starter-repo-main\data\formatted_output.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

daily_sales = (
    df.groupby("Date", as_index=False)["Sales"]
    .sum()
)

# Create chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales"
)

fig.update_traces(
    line=dict(width=4)
)

fig.add_vline(
    x="2021-01-15",
    line_width=3,
    line_dash="dash",
    annotation_text="Price Increase",
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0B1020",
    plot_bgcolor="#161B2E",
    font=dict(color="white"),
    xaxis_title="Date",
    yaxis_title="Sales ($)",
    title="Sales Trend Before and After Price Increase",
)

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#0B1020",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Segoe UI"
    },
    children=[

        html.Div(
            [
                html.Img(
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiEl3CX6D3COR0-_M90tVnQEBcroea7VhTjw&s",
                    style={
                        "height": "70px",
                        "marginRight": "20px"
                    }
                ),

                html.Div([
                    html.H1(
                        "Soul Foods Sales Dashboard",
                        style={
                            "color": "white",
                            "marginBottom": "5px"
                        }
                    ),

                    html.P(
                        "Impact Analysis of Pink Morsel Price Increase",
                        style={
                            "color": "#B8B8B8"
                        }
                    )
                ])
            ],
            style={
                "display": "flex",
                "alignItems": "center",
                "marginBottom": "40px"
            }
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.H3("Business Question"),
                        html.P(
                            "Were sales higher before or after the 15 Jan 2021 price increase?"
                        )
                    ],
                    style={
                        "backgroundColor": "#161B2E",
                        "padding": "20px",
                        "borderRadius": "15px",
                        "color": "white",
                        "marginBottom": "25px",
                        "borderLeft": "5px solid #6C5CE7"
                    }
                )
            ]
        ),

        html.Div(
            [
                dcc.Graph(
                    figure=fig
                )
            ],
            style={
                "backgroundColor": "#161B2E",
                "padding": "20px",
                "borderRadius": "15px",
                "boxShadow": "0 4px 20px rgba(0,0,0,0.3)"
            }
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
