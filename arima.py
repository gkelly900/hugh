import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import linregress
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from io import StringIO
import time, json
from datetime import date
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error

from matplotlib import rc
rc('text', usetex=False)

def test_stationarity(timeseries):   
    #Determing rolling statistics
    rolmean = timeseries.rolling(window=52,center=False).mean() 
    rolstd = timeseries.rolling(window=52,center=False).std()
    plt.figure(figsize=(12,8))
    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.xlabel("Year")
    plt.ylabel("Temperature (K)")
    plt.title('Vinther Rolling Standard Deviation')
    #plt.savefig("vint_rolling_stdev.jpg")
    
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    timeseries.dropna(inplace=True)
    dftest = adfuller(timeseries["Vint_Temp"], autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)


rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
matplotlib.style.use('ggplot')

df = pd.read_csv("hugh_data.csv")

df_vint = df[["Year", "Vint_Temp"]]
df_vint = df_vint.set_index("Year")


test_stationarity(df_vint)


