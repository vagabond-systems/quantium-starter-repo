from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load the data we processed in Task 2
df = pd.read_csv("pink_morsel_sales.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

app.layout = html.Div(className="dash-container", children=[
    html.Div(id='header', children=[
        html.H1('Pink Morsel Sales Visualizer')
    ]),

    html.Div(className='control-section', children=[
        html.Label("Filter by Region", className='control-label'),
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True
        ),
    ]),

    html.Div(children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales: {selected_region.capitalize() if selected_region != 'all' else 'All Regions'}",
        template="plotly_white",
        color_discrete_sequence=["#6366f1"]
    )
    
    # Modernize graph layout
    fig.update_layout(
        font_family="Outfit, sans-serif",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=60, b=40),
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="#f1f5f9")
    )
    
    # Add a vertical line for the price increase date (Jan 15, 2021)
    fig.add_shape(
        type="line",
        x0="2021-01-15", x1="2021-01-15",
        y0=0, y1=1, yref="paper",
        line=dict(color="#f43f5e", dash="dash", width=2)
    )
    fig.add_annotation(
        x="2021-01-15", y=1.05, yref="paper",
        text="Price Increase", showarrow=False, xanchor="left",
        font=dict(color="#f43f5e", size=12, weight=600)
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)