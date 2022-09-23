import pandas as pd

df1 = pd.DataFrame({'name':['a', 'b', 'c'], 'val1':[1, 2, 3]})
df2 = pd.DataFrame({'name':['b', 'c', 'd'], 'val2':[4, 5, 6]})

df1
df2

df1.merge(df2, on='name', how='outer')

df1.merge(df2, on='name', how='inner')

df1.merge(df2, on='name', how='left')

df1.merge(df2, on='name', how='right')

df1.merge(df2, on='name', how='left')
df2.merge(df1, on='name', how='right')

#slide 12
df3 = pd.DataFrame({'name':['a', 'a', 'b'], 'val3':[7, 8, 9]})
df3
df1.merge(df3, on='name', how='left')

df1.merge(df3, on='name', how='left', validate='one_to_one')

#slide 15
start_len = len(df1)
df_merged = df1.merge(df2, on='name', how='outer')
end_len = len(df_merged)

assert(start_len == end_len), 'Unexpected dataframe expansion after merge'

#slide 17

df_merged = df1.merge(df2, on='name', how='outer', indicator=True)




df_merged

df_merged.dtypes
df_merged['_merge']
df_merged[df_merged['_merge'] != 'both']

#slide 20
df4 = pd.DataFrame({'NAMES':['a', 'b', 'c'], 'val4':[10, 11, 12]})
df4
df1.merge(df4, left_on='name', right_on='NAMES', how='inner')

#slide 21
df5 = pd.DataFrame({'name':['a', 'a', 'b', 'b'],
                    'month':[1, 6, 1, 6],
                    'val5':[13, 14, 15, 16]})

df6 = pd.DataFrame({'name':['a', 'a', 'b', 'b'],
                    'month':[1, 6, 1, 6],
                    'val6':[17, 18, 19, 20]})

df5
df6
df5.merge(df6, on=['name', 'month'], how='inner')

#slide 22
df7 = pd.DataFrame({'name':['d', 'e', 'f'], 'val1':[21, 22, 23]})
df1
df7

pd.concat([df1, df7])

#slide 23

df = pd.DataFrame({'student':['A', 'B', 'C'],
                   'grade2019':[4, 3.5, 3.75],
                   'grade2018':[4, 4, 3.5],
                   'grade2017':[3, 3, 3.5]})
df
pd.wide_to_long(df, stubnames='grade', i='student', j='year')

df = pd.DataFrame({'student':['A', 'B', 'C'],
                   '2019':[4, 3.5, 3.75],
                   '2018':[4, 4, 3.5],
                   '2017':[3, 3, 3.5]})
df
df.melt(id_vars='student', value_vars=None, var_name='year', value_name='grade')

#slide 27
df = df.melt(id_vars='student', value_vars=None, var_name='year', value_name='grade')
df

df.pivot(index='student', columns='year', values='grade')
