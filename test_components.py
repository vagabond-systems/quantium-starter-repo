import chromedriver_autoinstaller
from app import app

chromedriver_autoinstaller.install()


def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.wait_for_element_by_id("Header", timeout=2)

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.wait_for_element_by_id("RadioButton", timeout=2)

def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.wait_for_element_by_id("ProductSalesGraph", timeout=2)
