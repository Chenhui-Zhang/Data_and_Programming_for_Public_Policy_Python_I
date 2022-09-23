import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

df.mean()

df.groupby('clarity').mean()
df.groupby('clarity').mean().round(2)

#slide 5
df_clarity = df.groupby('clarity').mean().round(2).reset_index()
df_clarity.sort_values('clarity')

clarity_order = ['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 
                 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

category = pd.Categorical(df_clarity['clarity'], 
                          categories=clarity_order, 
                          ordered=True)
category
df_clarity['clarity'] = category
df_clarity.sort_values('clarity')

#slide 11
df['>1ct'] = df['carat'].map(lambda c: 1 if c > 1 else 0)
df.groupby(['clarity', '>1ct']).mean().round(2)

#slide 14
grouped = df.groupby('clarity')
grouped

grouped.groups
df.iloc[15]

grouped.get_group('I1')
grouped.describe()
grouped.apply(lambda g: g['price'].max())

#slide 21
df['cut'].str.upper()

df['cut'].str.replace('Ideal', 'Pretty OK I guess')

#slide 23
from numpy import NaN
data = {'col1':[NaN, 2, NaN, 4], 
        'col2':[NaN, 6, 7, 8], 
        'col3':[NaN, 10, 11, 12]}
df = pd.DataFrame(data)
df

df.dropna()
df.dropna(how='all')

df.dropna(axis=1, thresh=3)

df.fillna(0)
df.fillna(method='backfill')
df.fillna({'col1':100, 'col2':200, 'col3':300})
