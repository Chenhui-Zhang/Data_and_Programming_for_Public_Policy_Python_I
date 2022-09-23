import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

df = pd.read_csv(url_to_csv)

df
#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values?  How would you find the mean values
#   per type of flower (you don't actually have to implement this - we
#   will cover it next week)

#2. using one line of code, multiply every value by 100


#3. subset the data so only virginica flowers remain


#4. create a new column named "petal_area" which is equal to the length
#   times the width
