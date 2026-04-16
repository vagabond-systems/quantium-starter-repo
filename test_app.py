import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from app import app

def test_header_is_present(dash_duo):
    #header present
    dash_duo.start_server(app)
    
    #header render and verify
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales"

def test_visualisation_is_present(dash_duo):
    #visualised graph
    dash_duo.start_server(app)
    
    #auto get class
    dash_duo.wait_for_element(".dash-graph", timeout=10)
    assert dash_duo.find_elements(".dash-graph") is not None

def test_region_picker_is_present(dash_duo):
    #radio itmes
    dash_duo.start_server(app)
    
    #region filter
    dash_duo.wait_for_element("#region-filter", timeout=10)
    assert dash_duo.find_elements("#region-filter") is not None