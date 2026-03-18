import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback

# Load and prepare data
df = pd.read_csv('data_sales_data_1.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Initialize app
app = Dash(__name__, external_stylesheets=['https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap'])

app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Soul Foods Pink Morsel Sales Dashboard", 
                style={
                    'color': '#2c3e50', 'textAlign': 'center', 
                    'fontFamily': 'Roboto, sans-serif',
                    'fontWeight': 700, 'fontSize': '2.5em',
                    'marginBottom': '10px', 'textShadow': '2px 2px 4px rgba(0,0,0,0.1)'
                }),
        html.P("Interactive analysis of sales before/after 15 Jan 2021 price increase",
               style={
                   'color': '#7f8c8d', 'textAlign': 'center', 
                   'fontFamily': 'Roboto, sans-serif', 'fontSize': '1.1em',
                   'marginBottom': '30px'
               })
    ], className='header'),

    # Controls
    html.Div([
        html.Label("Filter by Region:", 
                  style={
                      'fontFamily': 'Roboto, sans-serif', 'fontWeight': 600, 
                      'color': '#2c3e50', 'fontSize': '1.1em', 'marginRight': '15px'
                  }),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={
                'display': 'block', 'margin': '8px 0', 'fontFamily': 'Roboto, sans-serif',
                'fontSize': '1em', 'cursor': 'pointer', 'color': '#34495e',
                'padding': '8px 12px', 'borderRadius': '6px', 
                'transition': 'all 0.2s ease'
            },
            style={'width': '300px'}
        )
    ], style={
        'background': 'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)',
        'padding': '25px', 'borderRadius': '12px', 
        'boxShadow': '0 4px 12px rgba(0,0,0,0.1)',
        'marginBottom': '30px', 'textAlign': 'center'
    }),

    # Chart
    html.Div([
        dcc.Graph(id='sales-chart')
    ], style={'padding': '20px', 'backgroundColor': '#ffffff'})

], style={
    'minHeight': '100vh', 'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'padding': '40px 20px', 'fontFamily': 'Roboto, sans-serif'
})

@callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df.copy()
        color_col = 'Region'
        showlegend = True
    else:
        filtered_df = df[df['Region'] == selected_region]
        color_col = None
        showlegend = False
    
    fig = px.line(filtered_df, x='Date', y='Sales', color=color_col,
                 title=f"Pink Morsel Sales Over Time ({'All Regions' if selected_region=='all' else selected_region.title()})",
                 labels={'Sales': 'Total Sales (£)', 'Date': 'Date'},
                 markers=True, height=650)
    
    # Add price increase marker
    fig.add_vline(x=pd.to_datetime('2021-01-15'), 
                  line_dash="dash", line_color="red", 
                  annotation_text="Price Increase (15 Jan 2021)",
                  annotation_position="top right")
    
    # Styling
    fig.update_layout(
        hovermode='x unified',
        font=dict(family="Roboto, sans-serif", size=12),
        plot_bgcolor='rgba(255,255,255,0.9)',
        paper_bgcolor='rgba(255,255,255,0.95)',
        title_font_size=20, title_x=0.5
    )
    
    fig.update_traces(line=dict(width=3), marker=dict(size=6))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
