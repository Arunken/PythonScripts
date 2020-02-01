# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:10:10 2018

@author: Ourabora
"""
# Q4
def solve(numheads,numlegs):
    ns = 'No solutions!'
    for i in range(numheads+1):
        j = numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads = 35
numlegs = 94
solution = solve(numheads,numlegs)
print('no of rabits : ',solution[0])
print('no of rabits : ',solution[1])

# Q5

from itertools import permutations
lis = [1,2,3]

perm = permutations(lis)
for i in list(perm):
    print(i)

# Q6 : print even indexed characters from a string 
    
s = input('enter a string')
for i in range(len(s)):
    if i%2==0:
        print(s[i])
        

# Q7 :
s = input('enter a string')
unch = set(s)
for ch in unch:
    count=0
    
    for i in s:
        if i==ch:
            count=count+1
    print('Occurence of ',ch,' in the string is ',count)
    
    
# Q8 :    
class Person: # by default this class extends object class
    def getGender(self):
        return 'person'


class Male(Person):
    def getGender(self):
        return 'Male'
    
class Female(Person):
    def getGender(self):
        return 'Female'
    
    
obj = Male()
gen = obj.getGender()
print(gen)




# Q9 :

lis = [12,24,35,24,88,120,155,88,120,155]
newlis =[]
seen = set()
for item not in li:
    if item not in seen():
        seen.add(item)
        newlis.append(item)

print(newli)

# Q10 :

lis1 =[1,3,6,78,88,35,55]
lis2 =[12,24,35,24,88,120,155]

s1 = set(lis1)
s2 = set(lis2)
s = s1 & s2
print(s)

# Q11 :

li =[12,24,35,70,88,120,155]
li = [x for(I,x) in  enumerate(li) if I not in(0,4,5)]

