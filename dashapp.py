from dash import Dash, Input, html, dcc, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Load data
df = pd.read_csv("cleaned_sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

# App Layout
app.layout = html.Div(style={
    'backgroundColor': '#0f172a',
    'color': 'white',
    'fontFamily': 'Arial',
    'padding': '20px'
}, children=[

    html.H1("📊 Pink Morsels Sales Dashboard", style={
        'textAlign': 'center',
        'marginBottom': '10px'
    }),

    html.P("Explore region-specific sales trends across time.", style={
        'textAlign': 'center',
        'marginBottom': '30px',
        'color': '#cbd5f5'
    }),

    # Radio Buttons
    html.Div([
        html.Label("Select Region:", style={'fontSize': '18px'}),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            labelStyle={'display': 'inline-block', 'marginRight': '15px', 'margintop': '5px', 'color': '#cbd5f5', 'horizontalAlign': 'center'}
        ),

    ], style={
        'textAlign': 'center',
        'marginBottom': '30px'
    }),

        html.Div([
        html.Label('Select Year', style={'fontSize': '18px', 'marginBottom': '10px'}),

        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(y), 'value': y} for y in df['year'].unique()],
            value=df['year'].min(),
            clearable=False,
            style={
                'width': '200px',
                'backgroundColor': '#1e293b',
                'color': 'white',
                'borderRadius': '5px'
            }
        )
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center'   # 👈 THIS centers the dropdown
    }),



    # Graph
    dcc.Graph(id='sales-line')

])


@app.callback(
    Output('sales-line', 'figure'),
    [
        Input('region-radio', 'value'),
        Input('year-dropdown', 'value')
    ]
)
def update_chart(selected_region, selected_year):
    
    filtered_df = df.copy()

    # Filter by region
    if selected_region != 'all':
        filtered_df = filtered_df[
            filtered_df['region'].str.lower() == selected_region
        ]

    # Filter by year
    filtered_df = filtered_df[filtered_df['year'] == selected_year]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color='region',
        title=f"Sales Trends - {selected_year}"
    )

    fig.update_layout(
        plot_bgcolor='#1e293b',
        paper_bgcolor='#0f172a',
        font_color='white'
    )

    return fig
if __name__ == '__main__':
    app.run(debug=True, dev_tools_hot_reload=False)
