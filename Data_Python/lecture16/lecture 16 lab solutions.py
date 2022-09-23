#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup

url = r'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path = r'c:\users\jeff levy\desktop\wiki_table.csv'

#from web to Python object
response = requests.get(url) #line that goes online
soup = BeautifulSoup(response.text, 'lxml') #does not go online

#from whole page to table
tables = soup.find_all('table')
print(len(tables))
print('Madonna' in tables[0].text)

#from table to lists of rows/cells
table = tables[0]
rows = table.find_all('tr')
# [r for r in rows]
cells = [r.find_all(lambda c: c.name in ['td', 'th']) for r in rows]

#from raw content to csv-suitable content
#text = [[t.text for t in c] for c in cells]
text = [[t.text.strip().replace('\n', ' ') for t in c] for c in cells]
print(text[1])
text_rows = [','.join(t) for t in text]
text_body = '\n'.join(text_rows)

with open(path, 'w') as ofile:
    ofile.write(text_body)
