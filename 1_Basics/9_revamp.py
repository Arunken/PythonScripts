# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:18:16 2018

@author: Arken
"""

# splitting a sentence and storing it in a list or tuple

a = ' python programming '
a = a.strip()
b = list(a) #saves individual characters separately in a list.
c = tuple(b) # The same goes for tuple.

tup = a.split() # split in to individual words

tup1 = a.split('o') # split wherever a specific character is present

st = ','.join(tup1) # joins the items in the list and adds a comma in between


d = 'python programming on'
e = d[8:19:3] # values between 8 and 19 and return every 3rd value


f = ['hi','I','am','learning','python','programming'] # list
for i in f:
    print(i) # prints each element in the list
    
for i in f:
    if 'hi' in f:
        print(i) # print each element in the list if a specific condition is satisfied
    else:
        print('ok thank you') # else print a message
        

g = [1,2,3,4,5,6,7,8,9,10]
for i in g:
    if i%2==0:
        print(i) # print even numbers in the list
        

for i in range(0,len(g),2):
    print(i) # print every 2nd value between 0 and 10
    
    
    
for i in range(0,10):
    if 2<i<9:
        print(i)
    else:
        print('help me')