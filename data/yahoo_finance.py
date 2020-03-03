# reference : https://pypi.org/project/yfinance/

import yfinance as yf
import json

msft = yf.Ticker("MSFT")

# get stock info
stock_info = msft.info

# parsed = json.loads(stock_info)
print(json.dumps(stock_info,
                 indent=4,
                 sort_keys=True))
