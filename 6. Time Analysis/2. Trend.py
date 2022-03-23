import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
#1. Extract Formatted Date
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], 
	index_col='Month',date_parser=dateparse)
ts = data['#Passengers'] 
#Specify the entire range:
print(ts['1949-01-01':'1949-05-01'])
#Use ':' if one of the indices is at ends:
print(ts[:'1949-03-01'])
#2. Apply Exponential Logarithm on data
ts_log = np.log(ts)
#3. Find Moving Averages
moving_avg = ts_log.rolling(12).mean()
plt.plot(ts_log)
plt.plot(moving_avg, color='red')
plt.show()