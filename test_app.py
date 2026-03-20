from app import app
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# Configure chrome options for headless mode in this environment
@pytest.fixture(scope="package")
def pytest_setup_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options

# Note: dash_duo uses the chromedriver in PATH. 
# We'll need to add the downloaded driver to PATH.
os.environ["PATH"] += os.pathsep + os.path.dirname(ChromeDriverManager().install())

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("#header").text == "Pink Morsel Sales Visualizer"

def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart") is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)
    assert dash_duo.find_element("#region-picker") is not None
