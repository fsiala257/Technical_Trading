import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('fivethirtyeight')


class tradingBot:

    def readFile(self,fileName):
        df = pd.read_csv(fileName)
        return df;

    def SMA(self,data,period,column='Close'):
        return data[column].rolling(window=period).mean()

    def EMA(self,data,period,column='Close'):
        return data[column].ewm(span=period,adjust=False).mean()

    



bot1 = tradingBot()
df = bot1.readFile('BTCUSDT.csv')
df2 = bot1.SMA(df,120)
df3 = bot1.EMA(df,120)


plt.plot(df['Close'])
plt.plot(df3)
plt.show()




# # MOVING AVERAGE CONVERGENCE/DIVERGENCE
# def MACD(data,period_long=26,period_short=12,period_signal=9, column='Close'):
#     # SHORT TERM EMA
#     shortEMA = EMA(data,period_short,column=column)
#     # LONG TERM EMA
#     longEMA = EMA(data,period_long,column=column)
#     # MACD
#     data['MACD'] = shortEMA - longEMA 
#     # SIGNAL
#     data['Signal_Line'] = EMA(data,period_signal,column='MACD')

#     return data

# # RELATIVE STRENGTH INDICATOR
# def RSI(data,period=14,column='Close'):
#     delta = data[column].diff(1) 
#     delta = delta[1:]
#     up = delta.copy()
#     down = delta.copy()
#     up[up<0] = 0
#     down[down>0] = 0
#     data['up'] = up
#     data['down'] = down
#     AVG_Gain = SMA(data,period,column='up')
#     AVG_Loss = abs(SMA(data,period,column='down'))
#     RS = AVG_Gain/AVG_Loss
#     RSI = 100.0-(100.0/(1.0+RS))
#     data['RSI'] = RSI
#     return data