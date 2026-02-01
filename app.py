#!/usr/bin/env python3
"""
Soul Foods – Pink Morsel Sales Visualiser
Dash app with region filtering and a polished dark-editorial theme.
"""

import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output

# ──────────────────────────────────────────────
# Load & prepare data
# ──────────────────────────────────────────────
df = pd.read_csv("data/pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)
df["region"] = df["region"].str.strip().str.lower()

PRICE_INCREASE_DATE = pd.Timestamp("2021-01-15")

# ──────────────────────────────────────────────
# Colour palette
# ──────────────────────────────────────────────
COLORS = {
    "bg_page":       "#0f1117",
    "bg_card":       "#1a1d27",
    "border":        "#2e3244",
    "text_primary":  "#eef0f4",
    "text_secondary":"#7a7f95",
    "accent_pink":   "#f43f5e",
    "accent_blue":   "#3b82f6",
    "accent_green":  "#22c55e",
    "accent_red":    "#ef4444",
}


# ──────────────────────────────────────────────
# Helper: build figure for a given region filter
# ──────────────────────────────────────────────
def build_figure(region_value):
    if region_value == "all":
        subset = df
    else:
        subset = df[df["region"] == region_value]

    daily = subset.groupby("date", as_index=False)["sales"].sum()
    before = daily[daily["date"] < PRICE_INCREASE_DATE]
    after  = daily[daily["date"] >= PRICE_INCREASE_DATE]

    fig = go.Figure()

    # Before trace
    fig.add_trace(go.Scatter(
        x=before["date"], y=before["sales"],
        mode="lines", name="Before Price Increase",
        line=dict(color=COLORS["accent_blue"], width=2.5),
        hovertemplate="<b>%{x|%d %b %Y}</b><br>Sales: $%{y:,.0f}<extra>Before</extra>",
    ))

    # After trace
    fig.add_trace(go.Scatter(
        x=after["date"], y=after["sales"],
        mode="lines", name="After Price Increase",
        line=dict(color=COLORS["accent_pink"], width=2.5),
        hovertemplate="<b>%{x|%d %b %Y}</b><br>Sales: $%{y:,.0f}<extra>After</extra>",
    ))

    y_max = daily["sales"].max() if len(daily) else 1

    # Reference line
    fig.add_shape(
        type="line",
        x0=PRICE_INCREASE_DATE, x1=PRICE_INCREASE_DATE,
        y0=0, y1=y_max * 1.12,
        line=dict(color=COLORS["text_secondary"], width=1.5, dash="dash"),
    )

    # Annotation
    fig.add_annotation(
        x=PRICE_INCREASE_DATE, y=y_max * 1.07,
        text="▲ Price Increase  15 Jan 2021",
        showarrow=False,
        font=dict(size=11, color=COLORS["text_secondary"]),
        xanchor="left", yanchor="top",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            title="Date",
            title_font=dict(size=13, color=COLORS["text_secondary"]),
            tickfont=dict(size=10, color=COLORS["text_secondary"]),
            showgrid=True, gridcolor=COLORS["border"],
            zeroline=False, showline=False,
        ),
        yaxis=dict(
            title="Total Sales ($)",
            title_font=dict(size=13, color=COLORS["text_secondary"]),
            tickfont=dict(size=10, color=COLORS["text_secondary"]),
            tickprefix="$", tickformat=",.0f",
            showgrid=True, gridcolor=COLORS["border"],
            zeroline=False, showline=False,
        ),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.03,
            xanchor="center", x=0.5,
            font=dict(size=12, color=COLORS["text_primary"]),
            bgcolor="rgba(0,0,0,0)",
        ),
        margin=dict(l=65, r=24, t=48, b=52),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#222633",
            font_size=12,
            font_color=COLORS["text_primary"],
            bordercolor=COLORS["border"],
        ),
    )

    return fig, before, after


# ──────────────────────────────────────────────
# KPI card factory
# ──────────────────────────────────────────────
def kpi_card(label, value_text, accent):
    return html.Div(
        style={
            "flex": "1",
            "background": COLORS["bg_card"],
            "borderRadius": "10px",
            "padding": "18px 20px",
            "border": f"1px solid {COLORS['border']}",
            "borderTop": f"3px solid {accent}",
        },
        children=[
            html.P(label, style={
                "margin": "0 0 6px 0",
                "fontSize": "11px",
                "color": accent,
                "fontWeight": "600",
                "textTransform": "uppercase",
                "letterSpacing": "1px",
            }),
            html.P(value_text, style={
                "margin": "0",
                "fontSize": "22px",
                "fontWeight": "700",
                "color": COLORS["text_primary"],
            }),
        ],
    )


# ──────────────────────────────────────────────
# App
# ──────────────────────────────────────────────
app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "background": COLORS["bg_page"],
        "fontFamily": "'Inter', 'Segoe UI', system-ui, sans-serif",
        "padding": "36px 24px 48px",
        "boxSizing": "border-box",
        "color": COLORS["text_primary"],
    },
    children=[

        # ── Header ──────────────────────────────────
        html.Div(
            style={
                "maxWidth": "920px",
                "margin": "0 auto 24px",
                "display": "flex",
                "alignItems": "center",
                "gap": "20px",
            },
            children=[
                html.Div(style={
                    "width": "52px", "height": "52px",
                    "borderRadius": "14px",
                    "background": f"linear-gradient(135deg, {COLORS['accent_pink']}, #c2185b)",
                    "display": "flex", "alignItems": "center", "justifyContent": "center",
                    "fontSize": "24px", "flexShrink": "0",
                }, children=["🍬"]),

                html.Div(children=[
                    html.H1("Pink Morsel Sales Dashboard", style={
                        "margin": "0 0 4px",
                        "fontSize": "22px",
                        "fontWeight": "700",
                        "color": COLORS["text_primary"],
                        "letterSpacing": "-0.3px",
                    }),
                    html.P("Soul Foods · Impact analysis of the Jan 15, 2021 price increase", style={
                        "margin": "0",
                        "fontSize": "13px",
                        "color": COLORS["text_secondary"],
                    }),
                ]),
            ],
        ),

        # ── Region filter card ──────────────────────
        html.Div(
            style={
                "maxWidth": "920px",
                "margin": "0 auto 20px",
                "background": COLORS["bg_card"],
                "borderRadius": "12px",
                "border": f"1px solid {COLORS['border']}",
                "padding": "16px 24px",
                "display": "flex",
                "alignItems": "center",
                "gap": "20px",
            },
            children=[
                html.Span("Region", style={
                    "fontSize": "11px",
                    "fontWeight": "600",
                    "color": COLORS["text_secondary"],
                    "textTransform": "uppercase",
                    "letterSpacing": "1px",
                    "whiteSpace": "nowrap",
                }),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All",   "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East",  "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West",  "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    className="region-radio",
                ),
            ],
        ),

        # ── Chart card ──────────────────────────────
        html.Div(
            style={
                "maxWidth": "920px",
                "margin": "0 auto 20px",
                "background": COLORS["bg_card"],
                "borderRadius": "12px",
                "border": f"1px solid {COLORS['border']}",
                "padding": "20px 22px 12px",
            },
            children=[
                dcc.Graph(
                    id="sales-chart",
                    style={"height": "400px"},
                    config={"displayModeBar": False},
                ),
            ],
        ),

        # ── KPI cards ───────────────────────────────
        html.Div(
            id="kpi-container",
            style={
                "maxWidth": "920px",
                "margin": "0 auto",
                "display": "flex",
                "gap": "14px",
            },
        ),
    ],
)




# ──────────────────────────────────────────────
# Callback – chart + KPIs react to region toggle
# ──────────────────────────────────────────────
@app.callback(
    Output("sales-chart", "figure"),
    Output("kpi-container", "children"),
    Input("region-filter", "value"),
)
def update_dashboard(region_value):
    fig, before, after = build_figure(region_value)

    avg_before = before["sales"].mean() if len(before) else 0
    avg_after  = after["sales"].mean()  if len(after)  else 0
    higher     = avg_after > avg_before

    cards = [
        kpi_card("Avg Daily Sales · Before", f"${avg_before:,.2f}", COLORS["accent_blue"]),
        kpi_card("Avg Daily Sales · After",  f"${avg_after:,.2f}",  COLORS["accent_pink"]),
        kpi_card(
            "Verdict",
            "Higher after ↑" if higher else "Lower after ↓",
            COLORS["accent_green"] if higher else COLORS["accent_red"],
        ),
    ]

    return fig, cards


# ──────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)