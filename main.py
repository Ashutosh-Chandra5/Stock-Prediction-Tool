import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

#for online Plotting

from plotly.offline import download_plotlyjs, plot, iplot


infosys = pd.read_csv(r'C:\Users\ashu3\PycharmProjects\StockPredictor\INFY.csv')
infosys.info()

infosys['Date'] = pd.to_datetime(infosys['Date'])
print(f'Dataframe contains stock prices between {infosys.Date.min()} {infosys.Date.max()}')
print(f'Total days = {(infosys.Date.max()) - infosys.Date.min()} days')
print(infosys.describe())
infosys[['Open', 'High', 'Low', 'Close', 'Adj Close']].plot( kind = 'box')
plt.show()
