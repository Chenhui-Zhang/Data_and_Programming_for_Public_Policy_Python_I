import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   March 2020 - January 2021 (technically not billed a recession but we'll include it anyway!)

path = r'D:\Spring2022\Data_Python\lecture13'
df = pd.read_csv(os.path.join(path, 'unrate.csv'), parse_dates=['DATE'])

recessions = [(datetime.datetime(2001, 3, 1),  datetime.datetime(2001, 11, 1)),
              (datetime.datetime(2007, 12, 1), datetime.datetime(2009, 6, 1)),
              (datetime.datetime(2020, 3, 1),  datetime.datetime(2021, 1, 1))]

fig, ax = plt.subplots(figsize=(12,6))
ax = df.plot(x='DATE', y='UNRATE', legend=False, ax=ax)

for start, end in recessions:
    ax.axvspan(start, end, alpha=0.4, color='gray')

#some tidying
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_title('US Unemployment Rate and Recessions')
ax.set_xlabel('')
ax.set_ylabel('Unemployment rate (SA)')

plt.show()
# fig.show()
# fig.clear()
#can also use plt.show() to replace both - one of the only places besides subplots that you can use plt
