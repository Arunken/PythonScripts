# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:31:54 2018

@author: Arken
"""

b = ['mango','strawberry','papaya','orange','grape']

b.append('berry')
print(b)

b1 = [1,2,3,4]
b.append(b1)

b[6][3]

b.extend(b1)
print(b)

b.extend("hello")
print(b)

b.insert(0,34)  # insert value 34 at index number 0. The other values in the list will be shifted accordingly
print(b)

print(b.count(34))  # return the count

b.remove("mango")  # deletes the first matching item. If there is no match an error will occur
print(b)


x=b.pop()
print(b.pop())  # pop method returns the value that is deleted using pop method. deletes the item at the last index
print(b)

y=b.pop(2)
print(b.pop(2))  # index can be specified to delete a specific item at a given index


c = ['goku','adith','sasi','arun','jasmine','sam','sylvia']
c.sort()
print(c)

c.reverse()
print(c)

li = ['we','are','all','one']

s = '-'.join(li)



del c
#del c['sasi','jasmine']
print(c)

