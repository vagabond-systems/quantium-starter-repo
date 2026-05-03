from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from dashapp import update_chart

def test_update_chart():
    # Simulate the callback context
    context = copy_context()
    context.run(lambda: setattr(context_value, 'triggered', [{'prop_id': 'region-radio.value', 'value': 'north'}]))

    # Call the update_chart function with the simulated context
    figure = context.run(update_chart, 'north')

    # Check if the figure is a dictionary (Plotly figure)
    assert isinstance(figure, dict), "The output should be a dictionary representing the Plotly figure."
    # Check if the figure has the expected keys
    assert 'data' in figure, "The figure should contain a 'data' key."
    assert 'layout' in figure, "The figure should contain a 'layout' key."
    # Check if the data is a list
    assert isinstance(figure['data'], list), "The 'data' key should contain a list of traces."
    # Check if the layout has a title
    assert 'title' in figure['layout'], "The layout should contain a 'title' key."
    # Check if the title is a string
    assert isinstance(figure['layout']['title'], str), "The title should be a string."
    # Check if the title contains the selected year
    assert '2021' in figure['layout']['title'], "The title should contain the selected year (2021)."
    