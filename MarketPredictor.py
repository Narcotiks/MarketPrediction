import numpy as np
import pandas as pd
import datetime as dt
#from pandas.io import data, wb
import matplotlib.pyplot as plt

start_date = dt.datetime(2000, 1, 1)
end_date = dt.datetime(2016, 7, 28)
#Reading the data csv file I have of the historical data, and return a array with the contents
shares = pd.read_csv('AGL.csv', index_col='Date', parse_dates=['Date'])

#shares['Date'] = pd.to_datetime(shares['Date'])
shar = shares.loc['2016-1-1':'2016-7-28']
#mask = (shares['Date'] > start_date) & (shares['Date'] <= end_date)
print(shar)
shar['Close'].plot()


plt.show()