import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys

# 2) Display the describe() output JUST for group color=E, clarity=SI2

# 3) Display the max value for price in each group

# 4) Display the min value for price in each group