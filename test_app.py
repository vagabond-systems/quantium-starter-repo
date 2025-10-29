import pytest
from dash.testing.application_runners import import_app

# Import your Dash app (update "app" to match your main file name)
@pytest.fixture
def dash_app():
    return import_app("app")


def test_header_present(dash_duo, dash_app):
    """Verify that the header is rendered."""
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Dashboard", timeout=5)


def test_visualisation_present(dash_duo, dash_app):
    """Verify that the Plotly line chart is visible."""
    dash_duo.start_server(dash_app)
    chart = dash_duo.find_element(".js-plotly-plot")
    assert chart is not None, "Line chart not found"


def test_region_picker_present(dash_duo, dash_app):
    """Verify that the region radio buttons exist."""
    dash_duo.start_server(dash_app)
    radios = dash_duo.find_elements("input[type='radio']")
    assert len(radios) >= 5, "Region radio buttons missing"
