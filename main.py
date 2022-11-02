# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:33:05 2022

@author: rkhan
"""

# import requests
import pandas as pd
import matplotlib.pyplot as pyplot

# ticker = 'aapl'

# api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# res = requests.get(api)

# res_json = res.json()

# df = pd.DataFrame(res_json['Time Series (5min)']).transpose()

# df.index = pd.to_datetime(df.index)
# df['4. close'] = pd.to_numeric(df['4. close'])

# pyplot.plot(df.index, df['4. close'])

from yahoo_fin import stock_info as si

ticker = 'VOO'
live_price =  si.get_live_price(ticker)
table = si.get_quote_table(ticker)
data = si.get_data(ticker, start_date = "01/01/2010")

tickers = si.tickers_sp500()

pyplot.plot(data.index,data['close'])
