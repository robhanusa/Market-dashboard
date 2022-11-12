# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 08:33:05 2022

@author: rkhan
"""

import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si

tickers = ['VOO','VWO','VGK','VTWO']
labels = ['S&P 500', 'Emerging Markets ETF', 'Europe ETF', 'Russell 2000']
ticker = 'VOO'
live_price =  si.get_live_price(ticker)
data = si.get_data(ticker, start_date = "01/01/2010")

#table = si.get_quote_table(ticker)
#tickers_sp500 = si.tickers_sp500()

def ETF_info(ticker):
    live_price =  si.get_live_price(ticker)
    data = si.get_data(ticker, start_date = "01/01/2010")
    return live_price, data

def gen_plot(ticker, label, ax):
    live_price, data = ETF_info(ticker)
    ax.plot(data.index,data['close'], label=label)
    ax.plot(data.index,[live_price for x in data.index], label='Current Price', 
         linestyle='--')
    ax.tick_params(axis='x', labelsize=8, rotation=45)
    ax.legend(prop=dict(size=7))

fig, axs = plt.subplots(2,2, sharex = True)
gen_plot(tickers[0], labels[0], axs[0,0])
gen_plot(tickers[1], labels[1], axs[0,1])
gen_plot(tickers[2], labels[2], axs[1,0])
gen_plot(tickers[3], labels[3], axs[1,1])

def ave_growth(ticker):
    #average annualized return per year
    current, data = ETF_info(ticker)
    start = data.open[0]
    years = (data.index[-1] - data.index[0]).days/365.25
    overall_return = (current-start)/start
    return (1+overall_return)**(1/years)-1
