import os
import sys
import pytest

# ensure repository root is on sys.path so tests can import app.py
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app, load_and_prepare


def start_dash(dash_duo):
    df = load_and_prepare()
    app = create_app(df)
    dash_duo.start_server(app)
    return dash_duo


def test_header_present(dash_duo):
    dd = start_dash(dash_duo)
    # wait for the header element
    h1 = dd.wait_for_element("h1.title", timeout=10)
    assert h1 is not None
    assert 'Soul Foods' in h1.text


def test_visualisation_present(dash_duo):
    dd = start_dash(dash_duo)
    # the dcc.Graph has id 'sales-graph'
    graph = dd.wait_for_element('#sales-graph', timeout=10)
    assert graph is not None


def test_region_picker_present(dash_duo):
    dd = start_dash(dash_duo)
    radio = dd.wait_for_element('#region-radio', timeout=10)
    assert radio is not None
