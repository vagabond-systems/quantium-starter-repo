import pytest
from dash.testing.application_runners import import_app

app = import_app("region")


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_page()

    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales"


def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_page()

   # visualization = dash_duo.wait_for_element_by_id("sales-chart", timeout=20) 

    visualization = dash_duo.find_element("#sales-chart")
    assert visualization.is_displayed()


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_page()

    region_picker = dash_duo.find_element("#region-button")
    assert region_picker.is_displayed()
