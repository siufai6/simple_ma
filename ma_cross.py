###
### a super simple ma cross backtesting system.
### requires pandas and pandas_datareader
###
import pandas as pd
from pandas_datareader.yahoo.daily import YahooDailyReader  as dr
## get data from yahoo into a dataframe
code='SPY'
data = dr(code,start='2000-01-01', interval='d').read()
        
short_ma_period = 50
long_ma_period = 200

#
ms = data.Close.rolling(short_ma_period).mean()
ml = data.Close.rolling(long_ma_period).mean()

# a simple "golden cross" for long trades
buy =  (ms > ml) * 1
sell =  (ms <= ml) *-1

# assume we close and open a trade with open price
# and.. is it profitable?
long_equity = (buy*data.Open.diff().shift()).sum() 
short_equity = (sell*data.Open.diff().shift()).sum()

print("short profit=%s" % (short_equity))
print("long profit=%s" % (long_equity))
