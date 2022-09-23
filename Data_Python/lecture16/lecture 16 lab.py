#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?
#robots.txt
#
#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup
url='https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path='D:\Spring2022\Data_Python\lecture16\data.csv'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
table=soup.find('table')
soup
table1=soup.find('table',{'class':'wikitable plainrowheaders sortable'})



for table in soup.find_all('table'):
    print(table.get('class'))