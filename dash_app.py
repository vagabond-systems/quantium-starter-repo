import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import pandas as pd

# Read the pink morsels sales data
df = pd.read_csv("pink_morsels_sales_data.csv")

# Ensure Date is a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Price increase date for analysis
price_increase_date = pd.to_datetime('2021-01-15', format='%Y-%m-%d')

# Compute pre- vs post-increase sales based on the provided data
pre_sum = df.loc[df['Date'] < price_increase_date, 'Sales'].sum()
post_sum = df.loc[df['Date'] >= price_increase_date, 'Sales'].sum().astype(int)

analysis_text = (
    f"""Sales before {price_increase_date}: {pre_sum:,.2f} $;
    Sales after {price_increase_date}: {post_sum:,.2f} $; """
)

if pre_sum > post_sum:
    conclusion = "Conclusion: Sales were higher before the price increase."
elif post_sum > pre_sum:
    conclusion = "Conclusion: Sales were higher after the price increase."
else:
    conclusion = "Conclusion: Sales were equal before and after the price increase."

# Build the Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center', 'marginTop': 20}),
    html.Div([
        html.Div([
            html.H3("Region", style={'padding': '5px', 'margin': '10px'}),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'north', 'value': 'north'},
                    {'label': 'south', 'value': 'south'},
                    {'label': 'east', 'value': 'east'},
                    {'label': 'west', 'value': 'west'},
                    {'label': 'all', 'value': 'all'},
                ],
                value='all',

            )
        ], style={
            'border': '1px solid #ddd'
        }),

        html.Div([
            html.H3("Summary"),
            html.P(analysis_text),
            html.P(conclusion)
        ], style={
            'padding-left': '15px',
        })
    ], style={
        'maxWidth': '700px',
        'margin': '0 auto',
        'padding': '20px',
        'border': '1px solid #ddd',
        'borderRadius': '5px',
        'backgroundColor': '#f9f9f9',
        'display': 'flex',

        'justifyContent': 'space-between',
    }),
    dcc.Graph(id='sales-graph'),
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(region_value):
    if region_value == 'all':
        title = 'Sales by Date - All Regions'
        # Aggregate sales by date (Line chart will use this)
        df_by_date = df.groupby('Date', as_index=False)['Sales'].sum()
    else:
        df_by_region = df[df['Region'] == region_value]
        df_by_date = df_by_region.groupby('Date', as_index=False)['Sales'].sum()
        title = 'Sales by Date - Region {}'.format(region_value)

    df_by_date = df_by_date.sort_values(by=['Date'])

    # Create a line chart with proper axis labels
    fig = px.line(df_by_date, x="Date", y="Sales", markers=True, title=title)
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales")

    return fig
if __name__ == '__main__':
    app.run(debug=True)