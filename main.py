import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('fivethirtyeight')


ticker = yf.Ticker('AAPL')
aapl_df = ticker.history(period = '1y')
aapl_df['Close'].plot(title="APPLE's stock price")

