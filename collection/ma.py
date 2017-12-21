import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import datetime as dt


def MACD(stock, start, end):
    df = pd.DataFrame(web.DataReader(stock, 'google', start, end)['Close'])
    df = df.reset_index()
    print(df)
    df['30 mavg'] = pd.rolling_mean(df['Close'], 30)
    df['26 ema'] = pd.ewma(df['Close'], span=26)
    df['12 ema'] = pd.ewma(df['Close'], span=12)
    df['MACD'] = (df['12 ema'] - df['26 ema'])
    df['Signal'] = pd.ewma(df['MACD'], span=9)
    df['Crossover'] = df['MACD'] - df['Signal']
    return stock, df['Date'][-1:].to_string(), df['Crossover'][-1:].mean()


# stocks = ['FB', 'AAPL', 'GOOG', 'AMZN', 'TSLA']
stocks = ['KRX:KOSPI']

d = []

for stock in stocks:
    stock, date, macd = MACD(stock, '1/1/2016', dt.datetime.today())
    d.append({'Stock': stock, 'Date': date, 'MACD': macd})

df2 = pd.DataFrame(d)
df2[['Date', 'Stock', 'MACD']]