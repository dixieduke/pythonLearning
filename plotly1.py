import plotly
import plotly.graph_objs as go 

plotly.offline.plot({
    "data": [go.Scatter(x=[1,2,3,4], y=[1,2,3,4])],
        "layout": go.Layout(title="line chart")
        }, auto_open=True)