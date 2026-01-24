

from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

data = pd.read_csv("final_data.csv")

def app_layout():
    return html.Div([
   
    html.H2("Pink Morsel sales of Souls Food", id="site_header",style={"fontFamily":"Times New Roman","margin-left":"65px","color":"#35317A"}),

    dcc.Graph(
        id="sales_graph"
        
    ),

    html.H4("Filter by region",style={"fontFamily":"Times New Roman","margin-left":"100px","color":"#35317A"}),
    dcc.RadioItems(["north", "south", "east", "west"],"north", id="region",  
                   style={"transform": "translateX(7em)", "fontSize":"18px","color":"#7911E1"})
   
    
],
style={'backgroundColor': '#E2E4F0', "padding":"20px"}
 
)


app.layout = app_layout()

@callback(
    Output(component_id='sales_graph', component_property='figure'),
    Input(component_id='region', component_property='value'))
def update_graph(region_name):
    df = data[data['region'] == region_name]
    fig = px.line(df, x="date", y = "sales")
    fig.update_layout(title_text = "Sales by date",title_x= 0.5,height=385, font_color="#C21815",
                      title_font_color="#1B1BDB"
                      )
    return fig





if __name__ == '__main__':
    app.run(debug=True)
