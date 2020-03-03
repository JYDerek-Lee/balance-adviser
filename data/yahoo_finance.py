# reference : https://pypi.org/project/yfinance/

import yfinance as yf
import json


class YahooFinance:
    def __init__(self,
                 tickers=None):
        self.tickers = tickers

    def __del__(self):
        pass

    def set_tickers(self,
                    tickers):
        if tickers is None:
            # logging error
            return None
        self.tickers = tickers


stocks = yf.download(tickers)
print(stocks.head())

msft = yf.Ticker("MSFT")

# get stock info
stock_info = msft.info

# get stock info
msft.info

#parsed = json.loads(stock_info)
print(json.dumps(stock_info,
                 indent=4,
                 sort_keys=True))

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
# opt = msft.option_chain('2020-03-03')
# data available via: opt.calls, opt.puts
