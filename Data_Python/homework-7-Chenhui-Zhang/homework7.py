# PPHA 30535
# Spring 2022
# Homework 7

# YOUR NAME HERE
# Chenhui Zhang

# YOUR CANVAS NAME HERE
# Chenhui Zhang

# YOUR GITHUB USER NAME HERE
# Chenhui-Zhang

# Due date: Sunday May 22nd before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data portals for the OECD and the World Bank.  Pick
# any three countries, and pick two data series from each of the OECD and the
# World Bank that covers these places over some time period.  It's ok if
# frequency doesn't match up (e.g. one is monthly and one is quarterly), but
# you will need to handle the aggregation.  Load the data into dataframes using
# Pandas data_reader, then merge the data together in long (tidy) format, and
# write it to a csv document that you commit to your repo.

import pandas_datareader.data as web
from pandas_datareader import wb
from pandas_datareader import oecd
import pandas as pd
import numpy as np

# Pick three countries: US, UK, Canada
# Two data series each: 
# From World Bank: GDP(current USD)
# From OECD: Central government debt
# Time period: 2000-2010, annual data

# Check robots.txt for web scraping permissions

# World Bank
country=['US','GB','CA']
indicator_gdp='NY.GDP.MKTP.CD'
df_wb_gdp=wb.download(indicator=indicator_gdp,country=country,start=2000, end=2010).reset_index()
df_wb_gdp.columns=['Country','Year','GDP(Source:World Bank)']
df_wb_gdp=df_wb_gdp.sort_values(by=['Country','Year'],ascending=[False,True])


# OECD
indicator_debt='GOV_DEBT'
df_oecd_debt=web.DataReader(indicator_debt,'oecd',start=2000,end=2010)
df_oecd_debt_us=df_oecd_debt['United States'].iloc[:,0].reset_index()
df_oecd_debt_us.insert(0,'Country','United States')
df_oecd_debt_us.columns=['Country','Year','Debt(Source:OECD)']
df_oecd_debt_uk=df_oecd_debt['United Kingdom'].iloc[:,0].reset_index()
df_oecd_debt_uk.insert(0,'Country','United Kingdom')
df_oecd_debt_uk.columns=['Country','Year','Debt(Source:OECD)']
df_oecd_debt_ca=df_oecd_debt['Canada'].iloc[:,0].reset_index()
df_oecd_debt_ca.insert(0,'Country','Canada')
df_oecd_debt_ca.columns=['Country','Year','Debt(Source:OECD)']
new_df_oecd_debt=pd.concat([df_oecd_debt_us,df_oecd_debt_uk,df_oecd_debt_ca])
new_df_oecd_debt['Year']=pd.DatetimeIndex(new_df_oecd_debt['Year']).year
new_df_oecd_debt['Year']=new_df_oecd_debt['Year'].astype(str)

df=df_wb_gdp.merge(new_df_oecd_debt)
df.to_csv('D:\Spring2022\Data_Python\homework-7-Chenhui-Zhang\question1.csv')
# Data Source: 
# https://data.worldbank.org/
# https://stats.oecd.org/
# Reference:
# https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
# https://docs.python.org/3/library/datetime.html


# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/programs-degrees/degrees/master-public-policy-mpp
# There is a list named Curriculumn after Program Details, explaining the core classes.
# There are 21 bullet points for this, beginning with "Analytical Politics I" and ending
# just before "Elective Options". Some of those bullet points are intented under others. 
# Using requests and BeautifulSoup, collect the text of each of these bullet points so 
# that the top level bullet points, e.g. "Analytical Politics I" are the keys in a 
# dictionary, while the bullet points representing specific classes under them are values
# in a list. The result will be a dictionary where you can index by a requirement and get
# back a list of core class options.

import requests
from bs4 import BeautifulSoup

url='https://harris.uchicago.edu/academics/degrees/master-public-policy-mpp'

# Check robots.txt for scraping permissions
# Yes, we are allowed. 

response=requests.get(url)
soup=BeautifulSoup(response.text, 'lxml')
ul_level1=soup.select('div.field__item.clearfix.text-formatted.field.field--name-field-body.field--type-text-long.field--label-hidden ul')[1]
all_li=[]
for item in ul_level1.select('p'):
    the_text=item.text
    all_li.append(the_text)

the_key=[]
for item in all_li:
    if 'PPHA' in item:
        the_key=the_key
    else:
        item=item.replace(':','')
        the_key.append(item)
# Removed the ':' at the end of the key to make the key tidier

the_value=[]
for item in ul_level1.select('ul'):
    the_text=item.text
    the_text=the_text.replace(', or','')
    the_text=the_text.replace('.','')
    the_text=the_text.replace('\xa0','')
    the_text=the_text.split('\n')
    while('' in the_text):
        the_text.remove('')
    the_value.append(the_text)
# Removed the word 'or', the period, and other html marks to make the value tidier

classes_dict={the_key[i]:the_value[i] for i in range(len(the_key))}   

# test the dictionary
# print(classes_dict['Analytical Politics I'])   

# Reference: 
# https://stackoverflow.com/questions/56069188/using-only-css-how-to-select-second-level-li
# https://stackoverflow.com/questions/46892032/how-to-get-the-first-ul-inside-div-having-a-class-name