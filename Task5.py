#!/usr/bin/env python
# coding: utf-8

# In[7]:


from Task4 import app
def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_line_chart(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#line-chart", timeout=10)


def test_region_selector(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-selector", timeout=10)


# In[ ]:





# In[ ]:




