# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 09:11:39 2018

@author: Kenrig
"""

# 1) =============== Python types to JSON strings and vice-versa
import json

di = {'1':'Arun','2':'Athul','3':'Sam'} 
jsonStr = json.dumps(di)
print(jsonStr)

dic = json.loads(jsonStr)
print(dic)


tu = (3,4,5,6,7,8,9,10)
jsonstr1 = json.dumps(tu)
print(jsonstr1)

tup = tuple(json.loads(jsonstr1))
print(tup)

li = [3,4,5,6,7,8,9,10]
jsonstr2 = json.dumps(li)
print(jsonstr2)

lis = json.loads(jsonstr2)
print(lis)

st = '[3, 4, 5, 6, 7, 8, 9, 10]'
jsonstr3 = json.dumps(st)
print(jsonstr3)

stri = json.loads(jsonstr3)
print(stri)


# 2) ============= load a url from internet and display the title and meta description tags


import requests
from bs4 import BeautifulSoup

url = input('Enter a website url : ')
url = 'https://'+url
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
soup.prettify()

title = soup.title
print(title)

metas = soup.find_all('meta')

list_meta = []
for link in metas:
    print(link)


# 3)============ Pick a site and try some web scraping to find stock prices


import requests # Library that will allow you to send HTTP requests using Python
from bs4 import BeautifulSoup # Python library for web scrapping(pulling data out of HTML and XML files)

url = "https://www.news18.com/stocks/indian-stocks-market-live/"
r = requests.get(url) # sending get request and saving the response as response object
soup = BeautifulSoup(r.content,'lxml') # Parameter 1 : HTML string to be parsed. Parameter 2 : name of the parser(optional)


# print(soup)
# print(soup.prettify())
  

data = soup.findAll('div',{"class":"sstab","id":"market_update_anc"}) 
#print(data) 
print(data[0].text)




# 4) ========= Extract only text and filter out script and meta tags========== 

import requests
from bs4 import BeautifulSoup

url = "https://www.wccftech.com"
r = requests.get(url) 
soup = BeautifulSoup(r.content,'lxml')


for script in soup(["script", "style", "title", "meta","head"]):
    script.extract()


text = soup.getText()

words = []
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
words.append(chunk for chunk in chunks if chunk)
for w in words:
    print(w)

text = ' '.join(chunk for chunk in chunks if chunk)    
#string1 =text.encode('utf-8')

lis1 = text.split(' ')
set1 = set(lis1)
countset1 = []

for w1 in set1:
    
    count = 0
    for w2 in lis1:
        if w1==w2:
            count+=1
    countset1.append(count)

for w,c in zip(set1,countset1):
    print('word : ',w,' count : ',c)

# 5) ========= Input a url and input a sentence containing the words that we wish to count in the content.
    # display these words along with their repetitions in the page
    
    

import requests
from bs4 import BeautifulSoup


inp = input('Enter the website address')
url = "https://"+inp
r = requests.get(url) 
soup = BeautifulSoup(r.content,'lxml')


for script in soup(["script", "style", "title", "meta","head"]):
    script.extract()


text = soup.getText()

words = []
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
words.append(chunk for chunk in chunks if chunk)
for w in words:
    print(w)

text = ' '.join(chunk for chunk in chunks if chunk)    
#string1 =text.encode('utf-8')

lis1 = text.split(' ')

sentence = input('Enter a sentence containing the words you wish to search : ')
words = sentence.split(' ')
set1 = set(words)
countset1 = []

for w1 in set1:
    
    count = 0
    for w2 in lis1:
        if w1==w2:
            count+=1
    countset1.append(count)

for w,c in zip(set1,countset1):
    print('word : ',w,' count : ',c)






