import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd

# Get the data
df = pd.read_csv("data/combined_sales_data.csv")

# Create the app
app = dash.Dash(__name__, external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.7.2/css/all.min.css", "https://fonts.googleapis.com/css?family=Open+Sans&display=swap"])

# Define colors for regions
region_colors = {
    "north": "#F94144",   # Modern red color
    "east": "#F3722C",    # Modern orange color
    "south": "#F9C74F",   # Modern yellow color
    "west": "#90BE6D",    # Modern green color
    "all": "#4D908E",     # Modern teal color
}

# Create the layout
app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "Pink Morsel Sales",
            style={
                "text-align": "center",
                "font-size": "48px",
                "color": "#333333",
                "margin-bottom": "20px",
            },
        ),
        html.Div(
            className="filters",
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "font-size": "18px",
                        "color": "#333333",
                        "margin-bottom": "10px",
                        "display": "block",
                    },
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {
                            "label": "All",
                            "value": "all",
                        },
                        {
                            "label": "North",
                            "value": "north",
                        },
                        {
                            "label": "East",
                            "value": "east",
                        },
                        {
                            "label": "South",
                            "value": "south",
                        },
                        {
                            "label": "West",
                            "value": "west",
                        },
                    ],
                    value="all",
                    className="radio-items",
                    labelStyle={
                        "display": "inline-block",
                        "margin-right": "10px",
                    },
                    inputClassName="radio-input",
                    labelClassName="radio-label",
                ),
            ],
        ),
        dcc.Graph(
            id="sales-graph",
            className="sales-graph",
        ),
    ],
)

# Create the callbacks
@app.callback(Output("sales-graph", "figure"), Input("region-filter", "value"))
def update_graph(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == region]

    # Create the figure
    figure = {
        'data': [
            {
                'x': filtered_df['Date'],
                'y': filtered_df['Sales'],
                'type': 'line',
                'line': {'color': region_colors.get(region, '#000000')},
            }
        ],
        'layout': {
            'title': 'Pink Morsel Sales',
            'xaxis_title': 'Date',
            'yaxis_title': 'Sales',
            'hovermode': 'x',
            'plot_bgcolor': '#F4F4F4',
            'paper_bgcolor': '#F8F8F8',
            'font': {'color': '#333333', 'family':'Open Sans'},
        },
    }

    return figure

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

