import pandas as pd
import plotly.express as px

def make_figure(df):
    fig = px.line(df, x='Date', y='Sales', title='Pink Morsels — Daily Sales',
                  labels={'Date':'Date', 'Sales':'Sales'})

    # add vertical marker for the price increase date
    # keep as a pandas Timestamp so Plotly can handle it natively
    vdate = pd.to_datetime('2021-01-15')

    # add a vertical line as a shape (avoids plotly's internal averaging bug)
    fig.add_shape(type='line', x0=vdate, x1=vdate, y0=0, y1=1,
                  xref='x', yref='paper', line=dict(color='red', dash='dash'))
    fig.add_annotation(x=vdate, y=1, yref='paper', showarrow=False,
                       text='Price increase 2021-01-15', xanchor='left', yanchor='bottom')
    fig.update_layout(hovermode='x unified')
    return fig
