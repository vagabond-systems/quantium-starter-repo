from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# 1. Load data
df = pd.read_csv("./formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# 2. Layout (Structure only, Styles come from CSS file)
app.layout = html.Div(children=[
    
    # Header Section
    html.Div(className='header', children=[
        html.H1('Pink Morsel Visualiser')
    ]),

    # Main content area
    html.Div(className='container', children=[
        
        # Filter Card
        html.Div(className='card', children=[
            html.H3("Select Region"),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all',
                inline=True,
                className='radio-buttons'
            ),
        ]),

        # Graph Card
        html.Div(className='graph-card', children=[
            dcc.Graph(id='sales-line-chart')
        ])
    ])
])

# 3. The Callback (Logic)
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
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
        title=f"Pink Morsel Sales: {selected_region.capitalize()} Region",
        labels={"sales": "Total Sales ($)", "date": "Date"}
    )

    # Use a consistent color for the line
    fig.update_traces(line_color='#e74c3c')
    
    # Add Price Increase Marker
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="#34495e")

    fig.update_layout(
        plot_bgcolor='white',
        xaxis_gridcolor='#ecf0f1',
        yaxis_gridcolor='#ecf0f1'
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)