import pytest
from dash import Dash
from dash import html
from dash import dcc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def app():
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Pink Morsel Sales"),
        dcc.Graph(id="sales-graph"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"}
            ]
        ),
    ])
    return app


def test_header_is_present(app):
    app.run_server(port=8050)
    wait = WebDriverWait(app.server, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert app.find_element(By.TAG_NAME, "h1").text == "Pink Morsel Sales"


def test_visualisation_is_present(app):
    app.run_server(port=8050)
    wait = WebDriverWait(app.server, 10)
    wait.until(EC.presence_of_element_located((By.ID, "sales-graph")))
    assert app.find_element(By.ID, "sales-graph").is_displayed()


def test_region_picker_is_present(app):
    app.run_server(port=8050)
    wait = WebDriverWait(app.server, 10)
    wait.until(EC.presence_of_element_located((By.ID, "region-filter")))
    assert app.find_element(By.ID, "region-filter").is_displayed()


if __name__ == "__main__":
    pytest.main()
