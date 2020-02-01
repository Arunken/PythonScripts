# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:31:01 2018

@author: Arken
"""

# Tuples are immutable which means you cannot update or change the values of tuple elements. 
# Removing individual tuple elements is not possible
# Entire tuple can be deleted using del tuplename
# Tuples are secured lists.

tup = ('mango','papaya','orange',4,'grape','strawberry')
a = tup[3]
tup[3] = 23 #error because tuples are immutable

b = list(tup) # converting tuple into a list

c = tuple(b) # converting list into a tuple

d = (1, 2, 3) + (4, 5, 6) # concatenation of tuples

print(d)

e = ('Hi!',) * 4 # repetition


f = len((1, 2, 3)) # Length property


g = 3 in (1, 2, 3) # Membership

lis  = (1,2,3)
for x in lis: # Iteration
    print(x)

h = (4,9,17,"Arun")
z = list(h)

i = h[2]
j = h[-2]
k = h[1:]


# Built-in functions

l = (4,9,17) # tuple
m = [4,9,17] # list

n = len(h) # returns length
o = max(h) # returns the max value
p = min(h)  # returns the min value
q = tuple(l) # converts thw list in to a tuple

# unpacking
x,y = ('hello','arun','sam','david') # stores the tuple values into variables x and y

# packing
a = 10,20,30


