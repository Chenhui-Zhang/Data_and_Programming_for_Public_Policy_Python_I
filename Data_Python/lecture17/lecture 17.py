import requests

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

url = r'https://ww2.energy.ca.gov/almanac/renewables_data/wind/index_cms.php'
response = requests.post(url)

response.text.find('Alta Wind VIII LLC')
response.text[32340:32550]

year = 2017
response = requests.post(url, data={'newYear':year})

response.text.find('Alta Wind VIII LLC')
response.text[34300:34550]

#slide 15
my_list  = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

my_list*3
my_array*3

my_list + my_list
my_array + my_array

np.concatenate((my_array, my_array))

np.stack((my_array, my_array), axis=0)

my_array.reshape(5, 1) #can use -1 instead of 5 to infer

np.array([1, 2, 'cat'])

#slide 21
mat = np.array([[1, 2], [3, 4], [5, 6]])
mat

mat[1]
mat[1][1]
mat[1, 1]

mat.T
mat.dot(mat.T)

np.linalg.pinv(mat)

mat.flatten()

#slide 25
df = sm.datasets.get_rdataset('Guerry', 'HistData').data
df.head()

model = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=df)
result = model.fit()
rs = result.summary()

rs
result.pvalues
result.params
result.rsquared

df['logpop'] = np.log(df['Pop1831'])
df['intercept'] = np.ones(len(df))
model = sm.OLS(endog=df['Lottery'], exog=df[['intercept', 'Literacy', 'logpop']])
result = model.fit()
result.summary()

