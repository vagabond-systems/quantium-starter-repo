from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# This helps dash_duo find the driver automatically
def pytest_setup_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Runs without opening a window
    return options

def test_001_header_exists(dash_duo):
    # 1. Start the app
    app = import_app("app")
    dash_duo.start_server(app)

    # 2. Wait for the header element (H1) and check if it's present
    # We look for the tag 'h1'
    dash_duo.wait_for_element("h1", timeout=10)
    
    # 3. Assert the header contains the correct text
    assert dash_duo.find_element("h1").text == "Pink Morsel Visualiser"

def test_002_visualisation_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # We look for the id we gave our dcc.Graph: 'sales-line-chart'
    # In CSS selectors, IDs are prefixed with #
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    
    assert dash_duo.find_element("#sales-line-chart") is not None

def test_003_region_picker_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # We look for the id we gave our dcc.RadioItems: 'region-filter'
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    assert dash_duo.find_element("#region-filter") is not None