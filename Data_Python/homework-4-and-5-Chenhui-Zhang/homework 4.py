# PPHA 30535
# Spring 2022
# Homework 4 and 5

# YOUR NAME HERE
# Chenhui Zhang

# YOUR CANVAS NAME HERE
# Chenhui Zhang
# YOUR GITHUB USER NAME HERE
# Chenhui-Zhang

# Due date: Sunday May 8th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work. Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the two csv documents included in
# your repo.  In nst-est2019-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, 20 is a US region, and 40 is a US state. REGION
# is the fips code for the US region. STATE is the fips code for the US state
# The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nst-est2019-alldata.pdf
# Note that each question will build on the modified dataframe from the
# question before.

# Question 1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.  Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.
import os
import pandas as pd
base_path=r'D:\Spring2022\Data_Python\homework-4-and-5-Chenhui-Zhang'
path=os.path.join(base_path, 'nst-est2019-alldata.csv')
df=pd.read_csv(path)


#basic dataframe exploration
df.head()
df.tail()
df.shape
df.dtypes
df.info()
df.describe()

#Ref: https://www.analyticsvidhya.com/blog/2021/06/top-15-pandas-data-exploration-functions/

# Question 2: Your data only includes fips codes for states.  Use the us
# library to crosswalk fips codes to state abbreviations.  Keep only the
# state abbreviations in your data.
import us
state_mapping=us.states.mapping('fips','abbr')
state_mapping['01']

state_abbr=[]
for item in df['STATE']:
    if item==0:
        state_abbr+=['NA']
    if item!=0:
        two_digit_i=str(item).zfill(2)
        abbr=state_mapping[two_digit_i]
        state_abbr+=[abbr]
df['ABBR']=state_abbr
df=df.drop(['STATE'],axis=1)

# Question 3: Subset the data so that only observations for individual
# US states remain, and only state names and data for the population
# estimates in 2010-2019 remain.

#subset data so that only observations for individual US states remain
df_subset=df[df['ABBR']!='NA']

#subset that only state names and data for the population estimates in 2010-2019
df_subset_2=df_subset[['ABBR','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015','POPESTIMATE2016','POPESTIMATE2017','POPESTIMATE2018','POPESTIMATE2019']]

# Question 4: Reshape the data from wide to long, making sure you reset
# the index to the default values if any of your data is located in the index.
df_reshape=pd.wide_to_long(df_subset_2, stubnames='POPESTIMATE', i='ABBR', j='YEAR')
df_reshape=df_reshape.reset_index()

# Question 5: Open the state-visits.csv file, and fill in the VISITED column
# with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the file as a dataframe in
# Python, and merge the visited column into your population dataframe, only
# keeping values that appear in both dataframes.  Are any observations
# dropped from this?  Show code where you investigate your merge, and
# display any observations that weren't in both dataframes.

df_visit=pd.read_csv('state-visits.csv')
df_visit=df_visit.rename(columns={'STATE':'ABBR'})
#audit merge
start_len=len(df_subset_2)
df_merge=df_subset_2.merge(df_visit,on='ABBR',how='outer',indicator=True)
end_len=len(df_merge)
assert(start_len==end_len),'Unexpected dataframe expansion after merge'
#display any observations that weren't in both dataframes
df_merge[df_merge['_merge']!='both']
