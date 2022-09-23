import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm

series = ['CPMNACSCAB1GQDE', 'LRUNTTTTDEQ156S',
          'CPMNACSCAB1GQPL', 'LRUNTTTTPLQ156S']
df = web.DataReader(series, 'fred', start='1995-01-01', end='2019-10-01')

df = df.rename({'CPMNACSCAB1GQDE':'GDPGermany',
                'LRUNTTTTDEQ156S':'EMPGermany',
                'CPMNACSCAB1GQPL':'GDPPoland',
                'LRUNTTTTPLQ156S':'EMPPoland'}, axis=1)
df = df.reset_index()

df_long = pd.wide_to_long(df, ['GDP', 'EMP'], i='DATE',
                                              j='COUNTRY',
                                              suffix='\\w+')

#this data is from lecture 18.  explore it, plot the series, then when
#you've gotten to know it, look up how to apply an HP filter from the
#statsmodels library, and filter all four series. Hint: it will be
#easier to do on the wide df object than on the df_long object.

#what Pandas method would you need to use to apply the filter on df_long?
#what is wrong with the employment data from Poland?
