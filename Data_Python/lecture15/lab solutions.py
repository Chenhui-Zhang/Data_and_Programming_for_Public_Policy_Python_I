# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 1st 2021.

#Hint: https://www.alphavantage.co/support/#api-key
import pandas_datareader.data as web
import pandas as pd
import os
import numpy as np
import datetime

apikey = '6CEX93QYFF1AV1CD'
start = datetime.date(2019, 1, 1)
end = datetime.date(2021, 12, 1)
df = web.DataReader('TSLA', 'av-monthly', start=start, end=end,
                    api_key=apikey)

# 2. Create a new column that holds the rolling 3 month average.
df.index = pd.to_datetime(df.index)
df['close_3ma'] = df['close'].rolling(3).mean()

# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.
df_q = df.resample('QS').mean()

# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.
fig, ax = plt.subplots(figsize=(12,6))
x = df.index
ax.plot(x, df['close'], 'r-', label='Mean closing')
ax.plot(x, df['close_3ma'], 'b--', label='Mean closing, 3-mo MA')

ax.legend()
ax.set_title('Tesla monthly average closing stock price')
ax.set_xlabel('')
ax.set_ylabel('Price')

#remove spines?  add vlines for significant events?  change font or font size?
#change colors?  move legend outside of the axis lines? label max and min?

plt.show()
