import pytest
import dash
from dash import Dash
import dash.testing  # Dash 2.6+ testing framework
from app import app  # Import your Dash app

@pytest.mark.parametrize("test_id, selector, expected_text", [
    ("001", "h1", "Soul Foods Pink Morsel Sales Dashboard"),
])
def test_header_present(dash_duo: dash.testing.DashDuO, test_id, selector, expected_text):
    """Test 001: Verify header title is present and correct."""
    dash_duo.start_server(app)
    dash_duo.wait_for_no_elements(selector, timeout=10)
    header = dash_duo.find_element(selector)
    assert expected_text in header.text, f"Header should contain '{expected_text}'"
    assert dash_duo.get_logs() == [], "Browser console should show no errors"

def test_visualisation_present(dash_duo: dash.testing.DashDuO):
    """Test 002: Verify sales line chart is rendered."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    chart = dash_duo.find_element("#sales-chart")
    assert chart is not None, "Sales chart div should exist"
    assert dash_duo.get_logs() == [], "No JavaScript errors during chart render"

def test_region_picker_present(dash_duo: dash.testing.DashDuO):
    """Test 003: Verify region radio button picker is functional."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    # Verify all 5 radio options exist
    options = dash_duo.find_elements("#region-filter input[type='radio']")
    assert len(options) >= 5, "Should have at least 5 radio button options"
    
    # Test radio button interaction works
    dash_duo.select_dccradio("#region-filter", "north")
    dash_duo.wait_for_text_to_equal("#sales-chart .legendtext", "north", timeout=5)
    
    assert dash_duo.get_logs() == [], "No errors during region filter interaction"
