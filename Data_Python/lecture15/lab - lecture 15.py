# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 1st 2021.

#Hint: https://www.alphavantage.co/support/#api-key

import pandas as pd
import datetime
import pandas_datareader as web
from pandas_datareader import wb
import requests

url='https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TSLA&apikey=YPAMHV2BEQUWVR6W'
r=requests.get(url)
data=r.json()
print(data)

start=str(datetime.date(year=2019,month=1,day=1))
end=datetime.date(year=2021,month=12,day=1)

data['Monthly Time Series']['2010-07-30'][u'close']

# 2. Create a new column that holds the rolling 3 month average.

# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.

# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.
