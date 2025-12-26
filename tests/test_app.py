import pytest
from dash import html, dcc

from pink_morsels.web import create_app


def find_component_by_id(tree, id_value):
    # recursive search for component with matching id
    comp_id = getattr(tree, 'id', None)
    if comp_id == id_value:
        return tree
    # dash components sometimes store props in .props; also support .children attr
    props = getattr(tree, 'props', None)
    children = None
    if props is not None:
        children = props.get('children')
    else:
        children = getattr(tree, 'children', None)

    if children is None:
        return None
    if isinstance(children, (list, tuple)):
        for c in children:
            res = find_component_by_id(c, id_value)
            if res is not None:
                return res
    else:
        return find_component_by_id(children, id_value)
    return None


def find_component_by_type(tree, comp_type):
    # match based on class or by tag name fallback
    if hasattr(tree, '__class__') and tree.__class__ is comp_type:
        return tree

    # check children as above
    props = getattr(tree, 'props', None)
    children = None
    if props is not None:
        children = props.get('children')
    else:
        children = getattr(tree, 'children', None)

    if children is None:
        return None
    if isinstance(children, (list, tuple)):
        for c in children:
            res = find_component_by_type(c, comp_type)
            if res is not None:
                return res
    else:
        return find_component_by_type(children, comp_type)
    return None


@pytest.fixture
def app():
    return create_app()


def test_header_present(app):
    layout = app.layout
    h1 = find_component_by_type(layout, html.H1)
    assert h1 is not None
    children = getattr(h1, 'props', {}).get('children', getattr(h1, 'children', ''))
    assert 'Pink Morsels' in children


def test_visualisation_present(app):
    layout = app.layout
    graph = find_component_by_id(layout, 'sales-graph')
    assert graph is not None
    assert isinstance(graph, dcc.Graph)


def test_region_picker_present(app):
    layout = app.layout
    picker = find_component_by_id(layout, 'region-picker')
    assert picker is not None
    assert isinstance(picker, dcc.RadioItems)
