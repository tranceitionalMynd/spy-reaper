# Spy Reaper

An algorithmic trading application based off of Interactive Brokers Python API.  This application connects to a running instance of Interactive Brokers' TWS (Trader Workstation) or Gateway.

The strategy of the trading algorithm is based off of the mean reversion trading theory, which states that stock prices, as they fluctuate, have a tendency to gravitate toward their mean (average) price.

The purpose of the algorithm is to manipulate mean reversion movements by stochastic analysis of stock price. When the stochastics are below a threshold, the algorithm will buy the stock.  When the stochastics become high again, the algorithm will sell the stock.

The goal of the algorithm is to outperform the S&P 500, while simultaneously minimizing risk.

The manipulated stock is SPY- the S&P 500 ETF.

Requires:
* Python 3
* pandas
* TWS API 973.05 installed under a system path or '/opt/ibapi-beta/'
* A running TWS or IB Gateway application to connect to

Project Status:
* Initial development
