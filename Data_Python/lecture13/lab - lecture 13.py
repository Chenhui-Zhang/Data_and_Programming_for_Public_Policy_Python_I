import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   March 2020 - January 2021 (technically not billed a recession but we'll include it anyway!)

df = pd.read_csv('unrate.csv', parse_dates=['DATE'])

recessions = [(datetime.datetime(2001, 3, 1),  datetime.datetime(2001, 11, 1)),
              (datetime.datetime(2007, 12, 1), datetime.datetime(2009, 6, 1)),
              (datetime.datetime(2020, 3, 1),  datetime.datetime(2021, 4, 1))]
