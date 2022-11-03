# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:33:05 2022

@author: rkhan
"""

import pandas as pd
import matplotlib.pyplot as plt

from yahoo_fin import stock_info as si

ticker = 'VOO'
live_price =  si.get_live_price(ticker)
table = si.get_quote_table(ticker)
data = si.get_data(ticker, start_date = "01/01/2010")

tickers = si.tickers_sp500()

plt.plot(data.index,data['close'])
plt.plot(data.index,[live_price for x in data.index])