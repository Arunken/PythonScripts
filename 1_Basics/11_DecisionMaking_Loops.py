# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:01:44 2018

@author: Ourabora
"""

    # If the given string contains a specific word

a = 'we are all one'

if 'we' in a:
    print('true')
    
else:
    print('false')
    
    
    # numeric
    
if (2>3): # can be written without brackets as well
    print('greater')
    
else:
    print('less')
    
    # elif(else if) condition in python
    
if 2>5:
    print('2>5')
elif 5>2:
    print('5>2')
    
    # while loop

i=0
while i<len(a):
    print(a[i])
    i = i+1
    
    # infinite while
var =1
while var == 1:
    num = input('Enter the password')
    if num=='12345':
        print('successful login')
        break # break and continue keywords are the same
    
    else:
        print('wrong password')
        
    # using else statement with while loop
        
while 2>31:
    print('greater')
else:
    print('less')
    
    
    # for loops and strings
    
a = 'we are all one'

for i in a:
    print(i)
    
    # using range with for loops
    
for i in range(3,9):
    print(i)
    

    
    
    # for loops and lists
    
    lis = ['banana','strawberry','mango','grape','papaya']
    for i in lis:
        print(i)
        
    # pass keyword
    
    for i in range(0,10):
        pass # acts as a placeholder. if not present in empty loops or unimplemented methods, exception will be raised 

if 2<3:
    pass     
    