#!/usr/bin/env python3
"""
Soul Foods - Pink Morsel Sales Visualiser
Dash application to visualise Pink Morsel sales data and analyse
the impact of the price increase on January 15, 2021.
"""

import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

# ──────────────────────────────────────────────
# Load & prepare data
# ──────────────────────────────────────────────
df = pd.read_csv("data/pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

# Aggregate total sales per date (all regions combined)
daily = df.groupby("date", as_index=False)["sales"].sum()

# Price-increase reference date
PRICE_INCREASE_DATE = pd.Timestamp("2021-01-15")

# ──────────────────────────────────────────────
# Build the figure
# ──────────────────────────────────────────────
fig = go.Figure()

# --- Before price increase (blue) ---
before = daily[daily["date"] < PRICE_INCREASE_DATE]
fig.add_trace(
    go.Scatter(
        x=before["date"],
        y=before["sales"],
        mode="lines",
        name="Before Price Increase",
        line=dict(color="#3b82f6", width=3),
    )
)

# --- After price increase (rose / pink) ---
after = daily[daily["date"] >= PRICE_INCREASE_DATE]
fig.add_trace(
    go.Scatter(
        x=after["date"],
        y=after["sales"],
        mode="lines",
        name="After Price Increase",
        line=dict(color="#f43f5e", width=3),
    )
)

# --- Vertical reference line on Jan 15 ---
fig.add_shape(
    type="line",
    x0=PRICE_INCREASE_DATE,
    x1=PRICE_INCREASE_DATE,
    y0=0,
    y1=daily["sales"].max() * 1.1,
    line=dict(color="#6b7280", width=2, dash="dash"),
)

# Annotation for the reference line
fig.add_annotation(
    x=PRICE_INCREASE_DATE,
    y=daily["sales"].max() * 1.05,
    text="Price Increase<br>15 Jan 2021",
    showarrow=False,
    font=dict(size=12, color="#6b7280"),
    xanchor="left",
    yanchor="top",
)

fig.update_layout(
    # Transparent background so the card styling shows through
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    # Axes
    xaxis=dict(
        title="Date",
        title_font=dict(size=14, color="#374151"),
        tickfont=dict(size=11, color="#6b7280"),
        showgrid=True,
        gridcolor="#e5e7eb",
        zeroline=False,
    ),
    yaxis=dict(
        title="Total Sales ($)",
        title_font=dict(size=14, color="#374151"),
        tickfont=dict(size=11, color="#6b7280"),
        tickprefix="$",
        tickformat=",.0f",
        showgrid=True,
        gridcolor="#e5e7eb",
        zeroline=False,
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5,
        font=dict(size=13, color="#374151"),
    ),
    margin=dict(l=70, r=30, t=50, b=60),
    hovermode="x unified",
)

# ──────────────────────────────────────────────
# Dash app layout
# ──────────────────────────────────────────────
app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "background": "#f3f4f6",
        "fontFamily": "'Segoe UI', system-ui, sans-serif",
        "padding": "32px 24px",
        "boxSizing": "border-box",
    },
    children=[
        # ── Header card ──
        html.Div(
            style={
                "maxWidth": "900px",
                "margin": "0 auto 28px auto",
                "background": "#ffffff",
                "borderRadius": "14px",
                "boxShadow": "0 2px 12px rgba(0,0,0,0.08)",
                "padding": "28px 32px",
                "borderLeft": "5px solid #f43f5e",
            },
            children=[
                html.H1(
                    "Soul Foods — Pink Morsel Sales Dashboard",
                    style={
                        "margin": "0 0 6px 0",
                        "fontSize": "24px",
                        "fontWeight": "700",
                        "color": "#1f2937",
                    },
                ),
                html.P(
                    "Analysing the impact of the January 15, 2021 price increase on Pink Morsel sales",
                    style={
                        "margin": "0",
                        "fontSize": "14px",
                        "color": "#6b7280",
                    },
                ),
            ],
        ),
        # ── Chart card ──
        html.Div(
            style={
                "maxWidth": "900px",
                "margin": "0 auto 28px auto",
                "background": "#ffffff",
                "borderRadius": "14px",
                "boxShadow": "0 2px 12px rgba(0,0,0,0.08)",
                "padding": "24px 28px",
            },
            children=[
                dcc.Graph(
                    id="sales-chart",
                    figure=fig,
                    style={"height": "420px"},
                    config={"displayModeBar": False},
                ),
            ],
        ),
        # ── Summary KPI cards ──
        html.Div(
            style={
                "maxWidth": "900px",
                "margin": "0 auto",
                "display": "flex",
                "gap": "16px",
            },
            children=[
                # Before
                html.Div(
                    style={
                        "flex": "1",
                        "background": "#eff6ff",
                        "borderRadius": "12px",
                        "padding": "20px 22px",
                        "borderTop": "3px solid #3b82f6",
                    },
                    children=[
                        html.P(
                            "Avg Daily Sales — Before",
                            style={"margin": "0 0 6px 0", "fontSize": "12px", "color": "#3b82f6", "fontWeight": "600", "textTransform": "uppercase", "letterSpacing": "0.5px"},
                        ),
                        html.P(
                            f"${before['sales'].mean():,.2f}",
                            style={"margin": "0", "fontSize": "26px", "fontWeight": "700", "color": "#1e40af"},
                        ),
                    ],
                ),
                # After
                html.Div(
                    style={
                        "flex": "1",
                        "background": "#fff1f2",
                        "borderRadius": "12px",
                        "padding": "20px 22px",
                        "borderTop": "3px solid #f43f5e",
                    },
                    children=[
                        html.P(
                            "Avg Daily Sales — After",
                            style={"margin": "0 0 6px 0", "fontSize": "12px", "color": "#f43f5e", "fontWeight": "600", "textTransform": "uppercase", "letterSpacing": "0.5px"},
                        ),
                        html.P(
                            f"${after['sales'].mean():,.2f}",
                            style={"margin": "0", "fontSize": "26px", "fontWeight": "700", "color": "#be123c"},
                        ),
                    ],
                ),
                # Verdict
                html.Div(
                    style={
                        "flex": "1",
                        "background": "#f0fdf4" if after["sales"].mean() > before["sales"].mean() else "#fef2f2",
                        "borderRadius": "12px",
                        "padding": "20px 22px",
                        "borderTop": "3px solid #22c55e" if after["sales"].mean() > before["sales"].mean() else "3px solid #ef4444",
                    },
                    children=[
                        html.P(
                            "Verdict",
                            style={"margin": "0 0 6px 0", "fontSize": "12px", "color": "#22c55e" if after["sales"].mean() > before["sales"].mean() else "#ef4444", "fontWeight": "600", "textTransform": "uppercase", "letterSpacing": "0.5px"},
                        ),
                        html.P(
                            "Sales were HIGHER after the price increase" if after["sales"].mean() > before["sales"].mean() else "Sales were LOWER after the price increase",
                            style={"margin": "0", "fontSize": "15px", "fontWeight": "700", "color": "#166534" if after["sales"].mean() > before["sales"].mean() else "#991b1b"},
                        ),
                    ],
                ),
            ],
        ),
    ],
)

# ──────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)