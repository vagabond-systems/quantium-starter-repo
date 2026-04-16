import pandas as pd
import plotly.graph_objects as go 
from dash import Dash, dcc, html 

df = pd.read_csv("formatted_data.csv", parse_dates=["date"])

df = df.groupby("date", as_index=False)["sales"].sum()
df = df.sort_values("date")

PRICE_INCREASE_DATE = "2021-01-15"

fig = go.Figure()

before = df[df["date"] < PRICE_INCREASE_DATE]
after = df[df["date"] >= PRICE_INCREASE_DATE]

fig.add_trace(go.Scatter(
    x=before["date"], y=before["sales"],
    mode="lines",
    name="Before Price Increase",
    line=dict(color="blue", width=1.5),
    hovertemplate="Date: %{x|%Y-%m-%d}<br>Sales: $%{y:.0f}<extra></extra>"  
))

fig.add_trace(go.Scatter(
    x=after["date"], y=after["sales"],
    mode="lines",
    name="After Price Increase",
    line=dict(color="red", width=1.5),
    hovertemplate="<b>Date: %{x|%Y-%m-%d}</b><br><b>Sales: $%{y:.0f}</b><extra></extra>"  
))
fig.add_vline(
    x=PRICE_INCREASE_DATE,
    line_width=2,
    line_dash="dash",
    line_color="black",
    annotation_text="Price Increase (15 Jan 2021)",
    annotation_position="top right",
    annotation_font=dict(size=12, color="black")
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Daily Sales (AUD)",
    hovermode="x unified",
    legend=dict(orientation="h", 
                yanchor="bottom", y=1.02, xanchor="right", x=1),
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#FFFFFF",
    font=dict(family="Inter, Arial, sans-serif", size=13),
    margin=dict(t=60, b=60, l=70, r=30),
)

fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=True, gridcolor="#EBEBEB", zeroline=False,
                 tickprefix="$", tickformat=",")

#layout app 

app = Dash(__name__)

app.layout = html.Div(id="root", children=[
    html.Header(id="header", children=[
        html.H1("Soul Foods – Pink Morsel Sales Visualiser", id="title"),
        html.P(
            "Daily Pink Morsel sales across all regions. "
            "The dashed red line marks the price increase on 15 January 2021.",
            id="subtitle",
        ),
    ]),
    html.Main(children=[
        dcc.Graph(
            id="sales-chart",
            figure=fig,
            config={"displayModeBar": False},
            style={"height": "520px"},
        )
    ]),
])

if __name__ == "__main__":
    app.run(debug=True)