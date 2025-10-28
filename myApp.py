from dash import Dash, html, dcc

import plotly.express as px

from script import DataClass # https://flexiple.com/python/import-class-from-another-file

myApp = Dash("Quant Project") # Constructor calling main Dash application class - initialising Dash web application

new_data_class = DataClass()
# Line graph with dataframe/.table mentioned, x + y axis values from dataframe columns 
# `color` shows Series/column to have different line plottings for - differentiated by colours
general_model= px.line(data_frame=new_data_class.combined_data_frame, x='date', y='sales', color= 'region') 

avg_line = px.line()



# `div` used in HTML for grouping similar sections of web page together
# `layout` used in HTML to define how page is sectioned: https://www.geeksforgeeks.org/html/html-layout/
myApp.layout = html.Div(children = [    # `children` [optional keyword to use here, can go without]: element nested in another upper value https://www.w3schools.com/jsref/prop_element_children.asp
    html.H1(children = "Soul Food's Analysis"),     # `H1`: header font - can have .H1, .H2. H3 etc. 
    html.Div(children = '''
             Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
             '''),
    dcc.Graph(
        id = 'all-data-graph',
        figure = general_model
    )
])

if __name__ == '__main__': # Main place to start Dash application
    myApp.run()



