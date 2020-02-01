# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:25:58 2018

@author: Ourabora
"""
import requests # Library that will allow you to send HTTP requests using Python
from bs4 import BeautifulSoup # Python library for web scrapping(pulling data out of HTML and XML files)



url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
r = requests.get(url) # sending get request and saving the response as response object
#r.content
soup = BeautifulSoup(r.content,'lxml') # Parameter 1 : HTML string to be parsed. Parameter 2 : name of the parser(optional)

print(soup)
print(soup.prettify())
print(soup.title)
print(soup.title.string)

# get all the hyperlinks and store in a list
list_href = []
for i in list_href:
    print(i)
links = soup.find_all("a") # to find the links
for link in links:
    #print(link)
    #print(link.get("href"))
    list_href.append(link.get("href"))
    
# scrap the required table
right_table = soup.find('table',{"class":"wikitable sortable plainrowheaders"}) 
print(right_table.prettify())   
print(type(right_table))


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells)==6:
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
        
import pandas as pd

df = pd.DataFrame()

df['Number'] = A
df['State/UT']=B
df['Admin capital']=C
df['legislative capital']=D
df['judiciary Capital']=E
df['year Capital was established']=F
df['Former capital']=G

df.to_csv('E:\\Documents\\PythonProjects\\1_Basics\\india.csv',encoding='utf-8',index=False)


# ==============Beautiful soup examples =======================================


from bs4 import BeautifulSoup 

data = '''<div class="image">
        <a href="http://www.example.com/eg1">Content1<img  
        src="http://image.example.com/img1.jpg" /></a>
        </div>
        <div class="image">
        <a href="http://www.example.com/eg2">Content2<img  
        src="http://image.example.com/img2.jpg" /> </a>
        </div>'''

soup = BeautifulSoup(data,'lxml')

for div in soup.findAll('div', attrs={'class':'image'}):
    print(div.find('a')['href']) 
    print(div.find('a').contents[0]) 
    print(div.find('img')['src']) 
    
    
# Example 2 =================================================================== 
    
from bs4 import BeautifulSoup

html_doc = '''<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>'''

soup = BeautifulSoup(html_doc, 'html.parser')
sistertags = soup.find_all(class_='sister')
for tag in sistertags:
    print(tag.text.strip())     
    
    
    
# Example 3 ====Extract only text and filter out script and meta tags==========    
    
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()
print(text_from_html(html))



# OR ===

import urllib
from bs4 import BeautifulSoup

url = "https://www.yahoo.com"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode('utf-8'))


class A:
    def __init__(self,s):
        self.s=s
        
    def print(self):
        print(self.s)
        
a = A()
a.print()

import re

sentence ="we are humans"
matched =re.match(r'(.*)(.*?)(.*)',sentence)
print(matched.group(2))




















    

