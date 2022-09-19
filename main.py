import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

# for online Plotting

from plotly.offline import download_plotlyjs, plot, iplot

infosys = pd.read_csv(r'C:\Users\ashu3\PycharmProjects\StockPredictor\INFY.csv')
infosys=infosys.fillna(0) #to remove null values



infosys['Date'] = pd.to_datetime(infosys['Date'])
print(f'Dataframe contains stock prices between {infosys.Date.min()} {infosys.Date.max()}')
print(f'Total days = {(infosys.Date.max()) - infosys.Date.min()} days')
print(infosys.describe())
infosys[['Open', 'High', 'Low', 'Close', 'Adj Close']].plot(kind='box')

# Setting the layout for plot
layout = go.Layout(
    title='Stock Prices of Infosys',
    xaxis=dict(title='Date',
               titlefont=dict(family='Courier New, monospace',
                              size=18,
                              color='#7f7f7f'
                              )
               ),

    yaxis=dict(
        title='Price',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

infosys_data = [{'x': infosys['Date'], 'y': infosys['Close']}]
plot1 = go.Figure(data=infosys_data, layout=layout)

# Building the regression
from sklearn.model_selection import train_test_split

# For preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# For model evaluation
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score

# Splitting the data
X = np.array(infosys.index).reshape(-1, 1)
Y = infosys['Close']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)

# Feature scaling
scaler = StandardScaler().fit(X_train)

from sklearn.linear_model import LinearRegression

# creating a linear model
lm = LinearRegression()
lm.fit(X_train, Y_train)

# plot the actual and predicted values
trace0 = go.Scatter(
    x=X_train.T[0],
    y=Y_train,
    mode='markers',
    name='Actual'
)
trace1 = go.Scatter(
    x=X_train.T[0],
    y=lm.predict(X_train).T,
    mode='lines',
    name='Predicted'
)

infosys_data=[trace0, trace1]
layout.xaxis.title.text = 'Day'
plot2 = go.Figure(data=infosys_data, layout=layout)
plot(plot2)
plt.show()


