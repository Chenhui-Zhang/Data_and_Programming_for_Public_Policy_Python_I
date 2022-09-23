from numpy import log, sqrt, NaN
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

log(10**2)
2 * log(10)

log(1)
log(0)
log(-1)

def ihs(x):
    return log(x + sqrt(x**2 + 1))

linear  = range(1, 11)
squared = [v**2 for v in linear]
logged  = [log(s) for s in squared]
ihsed = [ihs(s) for s in squared]

fig, ax = plt.subplots()
ax.plot(linear, squared, 'r-', label='squared')
ax.plot(linear, logged,  'b-', label='sq logged')
ax.plot(linear, ihsed, 'g-', label='sq ihs')
ax.legend()
plt.show()

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

#slide 9
fig, ax = plt.subplots()
for label, d in df_long.reset_index().groupby('COUNTRY'):
    d.plot(x='DATE', y='GDP', label=label, ax=ax)
ax.legend()
ax.set_title('GDP')

model = smf.ols('GDPGermany ~ GDPPoland ', data=df)
result = model.fit()
result.summary()

#slide 11
df['Germany_GDP_lfd'] = log(df['GDPGermany']) - log(df['GDPGermany'].shift())
df['Poland_GDP_lfd']  = log(df['GDPPoland'])  - log(df['GDPPoland'].shift())

fig, ax = plt.subplots()
ax.plot(df['DATE'], df['Germany_GDP_lfd'], 'b-', label='Germany')
ax.plot(df['DATE'], df['Poland_GDP_lfd'], 'r-', label='Poland')
ax.legend()
ax.set_title('GDP')

model = smf.ols('Germany_GDP_lfd ~ Poland_GDP_lfd ', data=df)
result = model.fit()
result.summary()

df['Germany_GDP_pctchange'] = (df['GDPGermany'] - df['GDPGermany'].shift()) / df['GDPGermany'].shift()
df[['Germany_GDP_pctchange', 'Germany_GDP_lfd']].head(10)

#slide 18
df['GDPGermany_norm'] = ((df['GDPGermany'] - df['GDPGermany'].min()) /
                        (df['GDPGermany'].max() - df['GDPGermany'].min()))
df['GDPPoland_norm'] = ((df['GDPPoland'] - df['GDPPoland'].min()) /
                        (df['GDPPoland'].max() - df['GDPPoland'].min()))

fig, ax = plt.subplots()
ax.plot(df['DATE'], df['GDPGermany_norm'], 'b-', label='Germany')
ax.plot(df['DATE'], df['GDPPoland_norm'], 'r-', label='Poland')
ax.legend()
ax.set_title('Normalized GDP')

#slide 19
df['GDPGermany_std'] = (df['GDPGermany'] - df['GDPGermany'].mean()) /df['GDPGermany'].std()
df['GDPPoland_std'] = (df['GDPPoland'] - df['GDPPoland'].mean()) /df['GDPPoland'].std()

fig, ax = plt.subplots()
ax.plot(df['DATE'], df['GDPGermany_std'], 'b-', label='Germany')
ax.plot(df['DATE'], df['GDPPoland_std'], 'r-', label='Poland')
ax.legend()
ax.set_title('Standardized GDP')

#slide 20
df['GDPGermany_norm'].std()
df['GDPGermany_std'].std()

df['GDPGermany_norm'].max()
df['GDPGermany_std'].max()

df['GDPGermany_norm'].mean()
df['GDPGermany_std'].mean()

df['GDPGermany_norm'].min()
df['GDPGermany_std'].min()

#slide 22
df = pd.DataFrame({'one':[1, 2, NaN, 4, 5, NaN, 7],
                   'two':[2, 3, 4, 5, 6, NaN, 8]})

df.isnull().sum(axis=0)
df.isnull().sum(axis=1)

df.dropna()
df.dropna(axis=1)
df.dropna(how='all')
df.dropna(subset=['one', 'two'])
df.dropna(thresh=1)

#slide 29
df.fillna(100)
df.fillna(df.mean())
df['one'].fillna(df['two'])

df.ffill()
df.bfill()
df.interpolate(method='linear')
