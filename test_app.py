import os
import pytest
import chromedriver_autoinstaller

# Install ChromeDriver and add it to PATH
chromedriver_path = chromedriver_autoinstaller.install()
os.environ["PATH"] = (
    os.path.dirname(chromedriver_path)
    + os.pathsep
    + os.environ["PATH"]
)

from dash.testing.application_runners import import_app


@pytest.fixture
def dash_app():
    return import_app("app")


def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    header = dash_duo.find_element("h1")

    assert header is not None
    assert header.text == "Soul Foods Sales Dashboard"


def test_visualisation_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    graph = dash_duo.find_element("#sales-line-chart")

    assert graph is not None


def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    region_picker = dash_duo.find_element("#region-filter")

    assert region_picker is not None