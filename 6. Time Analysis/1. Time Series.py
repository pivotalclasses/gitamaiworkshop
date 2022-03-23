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
# plt.plot(ts_log)
# plt.plot(moving_avg, color='red')
# plt.show()
#4. Seasonal Decompose to find Trend and Seasonality
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts_log)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
#5. Plot them all
plt.subplot(411)
plt.plot(ts_log, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal,label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
#6. Finally fit data using ARIMA
from statsmodels.tsa.arima_model import ARIMA
ts_log_diff = ts_log - ts_log.shift()
ts_log_diff.dropna(inplace=True)
model = ARIMA(ts_log, order=(2, 1, 0))  
results_AR = model.fit(disp=-1)  
plt.plot(ts_log_diff)
plt.plot(results_AR.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-ts_log_diff)**2))
plt.show()