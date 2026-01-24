from visualisation import update_graph, app_layout

#testing the presence of header
def test_header():
    layout = app_layout()
    assert any(child.id == "site_header" for child in layout.children if hasattr(child, 'id'))
   


#testing presence of region picker
def test_picker():
    layout = app_layout()
    assert any(child.id == "region" for child in layout.children if hasattr(child, 'id'))

#testing presence of visualizer
def test_visualizer():
    layout = app_layout()
    assert any(child.id == "sales_graph" for child in layout.children if hasattr(child, 'id'))
    