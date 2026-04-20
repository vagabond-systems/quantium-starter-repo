import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

@pytest.fixture
def dash_duo_with_driver(dash_duo):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    dash_duo.driver = driver
    return dash_duo


def test_header_present(dash_duo_with_driver):
    from app import app

    dash_duo_with_driver.start_server(app)

    header = dash_duo_with_driver.find_element("h1")
    assert header is not None


def test_graph_present(dash_duo_with_driver):
    from app import app

    dash_duo_with_driver.start_server(app)

    graph = dash_duo_with_driver.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo_with_driver):
    from app import app

    dash_duo_with_driver.start_server(app)

    radio = dash_duo_with_driver.find_element("#region-filter")
    assert radio is not None