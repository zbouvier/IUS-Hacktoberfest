from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
from dataProcessor import parseLabels, parseLangs
import plotly.io as pio
import os 

years = parseLabels()
langs = parseLangs()

#make the plotly results

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
)

fig.add_trace(go.Bar(y = list(langs.values()), x = list(langs.keys()), showlegend=False),
              row=1, col=1)


fig.add_trace(go.Pie(values = list(years.values()), labels = list(years.keys())),
              row=1, col=2)


fig.update_layout(height=600)

pio.write_html(fig, 'index.html', auto_open=True)

