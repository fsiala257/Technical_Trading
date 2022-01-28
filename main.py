import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('fivethirtyeight')


# SIMPLE MOVING AVERAGE
def SMA(data,period=30,column='close'):
        return data[column].rolling(window=period).mean()

# EXPONENTIONAL MOVING AVERAGE
def EMA(data,period=20,column='close'):
    return data[column].ewm(span=period,adjust=False).mean()

# MOVING AVERAGE CONVERGENCE/DIVERGENCE
def MACD(data,period_long=26,period_short=12,period_signal=9, column='Close'):
    # SHORT TERM EMA
    shortEMA = EMA(data,period_short,column=column)
    # LONG TERM EMA
    longEMA = EMA(data,period_long,column=column)
    # MACD
    data['MACD'] = shortEMA - longEMA 
    # SIGNAL
    data['Signal_Line'] = EMA(data,period_signal,column='MACD')

    return data

# RELATIVE STRENGTH INDICATOR
def RSI(data,period=14,column='Close'):
    delta = data[column].diff(1) 
    delta = delta[1:]
    up = delta.copy()
    down = delta.copy()
    up[up<0] = 0
    down[down>0] = 0
    data['up'] = up
    data['down'] = down
    AVG_Gain = SMA(data,period,column='up')
    AVG_Loss = abs(SMA(data,period,column='down'))
    RS = AVG_Gain/AVG_Loss
    RSI = 100.0-(100.0/(1.0+RS))
    data['RSI'] = RSI
    return data