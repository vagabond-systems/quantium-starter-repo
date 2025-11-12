import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
import time

driver = webdriver.Chrome()


def wait_for_any_element(dash_duo, selectors, timeout=4):
    """
    Helper: wait for any of the given selectors to be present.
    Returns true if any selector is found within the timeout, False otherwise.
    :param dash_duo:
    :param selectors:
    :param timeout:
    :return:
    """

    for selector in selectors:
        try:
            dash_duo.wait_for_element(selector, timeout=timeout)
            return True
        except Exception:
            pass
    return False

def test_header_present(dash_duo):
    # Load the app from dash_module
    app = import_app('dash_app')
    dash_duo.start_server(app)

    header_selectors = [
        "#header",
        "header"
        "h1",
        ".header",
        "div[id='header']",
    ]

    wait_for_any_element(dash_duo, header_selectors), "Header element mot found on the page"

def test_visualization_present(dash_duo):
    app = import_app('dash_app')
    dash_duo.start_server(app)

    visualization_selectors = [
        "#visualization",
        "div[id='visualization']",
        "#visualization svg",
        "#graph",
        "#graph svg",
        ".visualization",
        "#svg#visualisation",
        "#sales-graph",
    ]

    assert wait_for_any_element(dash_duo, visualization_selectors, 4), "Visualization element found on the page"

def test_radio_button_present(dash_duo):
    app = import_app('dash_app')
    dash_duo.start_server(app)

    radio_button_selectors = [
        "#region-filter",
        "region-filter",
        ".region-filter",
        "div[id='region-filter']",
        "div[classname='region-filter']",
    ]

    assert wait_for_any_element(dash_duo, radio_button_selectors, 4), "Radio element not found on the page"


driver.quit()