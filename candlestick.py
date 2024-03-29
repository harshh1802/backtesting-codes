import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('ohlv.csv')

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.show()