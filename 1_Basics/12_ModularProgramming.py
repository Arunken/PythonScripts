# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:40:25 2018

@author: Arken
"""


# def keyword defines a function

def display():
    print('called the function')
    print(1)
    print(2)
    print(3)
    print(4)
    
print('going to call the function')
display()

# function with return value

def getvalue():
    print('hello')
    return 20

print(getvalue())
x = getvalue()
print('The value returned is ',x)

# returning multiple values

def getvalues():
    return 'arun','shakti'

a,b = getvalues() 


# passing parameters

def setvalues(x,y):
    print('x value :',x)
    print('y value :',y)
    
    
v1 = input("enter a value")
v2 = input("enter another value")
setvalues(v1,v2)


def findsum(x,y):
    z = x+y
    return z
    
    
v1 = int(input("enter a value"))
v2 = int(input("enter another value"))
s=findsum(v1,v2)


# A function that shows the results of running competitions consisting of 2 to 4 runners.
def save_ranking(first, second, third=None, fourth=None):
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)    

# Pass the 2 positional arguments
save_ranking('ming', 'alice')
# Pass the 2 positional arguments and 1 keyword argument
save_ranking('alice', 'ming', third='mike')
# Pass the 2 positional arguments and 2 keyword arguments (But, one of them was passed as like positional argument)
save_ranking('alice', 'ming', 'mike', fourth='jim')


def display(x=None,y=None,z=None):
    if x==None and y==None and z==None:
        print('1st method invoked')
    elif y==None and z==None:
        print('2nd method invoked')
    elif z==None:
        print('3rd method invoked')
    else:
        print('4th function invoked')
        
        
display()
        
    



 '''
 For positional arguments, it is not possible to omit it, and you must pass all 
 positional arguments to the correct location for each number of arguments declared.
 However, for keyword arguments, you can set a default value of it when declaring a
 function, and if you omit the argument, the corresponding default value is entered 
 as the value of the argument. That is, the keyword arguments can be omitted
 '''

 
 # variadic arguments
 # Variadic positional arguments
def save_ranking(*args):
    print(args) 
    
save_ranking('ming', 'alice', 'tom', 'wilson', 'roy')

# Variadic positional and keyword arguments
def save_ranking(*args, **kwargs):
    print(args) # tuple    
    print(kwargs) # dictionary
    
save_ranking('ming', 'alice', 'tom', fourth='wilson', fifth='roy')

'''
In above, *args means accepting the arbitrary numbers of positional arguments and
 **kwargs means accepting the arbitrary numbers of keyword arguments. In here,
 *args, **kwargs are called unpacking.
 
 Note : keyword arguments cannot be declared before positional arguments
'''


# For unpacking the containers

from functools import reduce

primes = [2, 3, 5, 7, 11, 13]

def product(*numbers):
    p = reduce(lambda x, y: x * y, numbers)
    return p 

product(*primes)


product(primes)


 '''
Because the product() take the variable arguments, we need to unpack the our list
 data and pass it to that function. In this case, if we pass the primes as *primes,
 every elements of the primes list will be unpacked, then stored in list called 
 numbers. If pass that list primes to the function without unpacking, the numbers 
 will has only one primes list not all elements of primes.
 
 Note : For tuple, it could be done exactly same to list, and for dict, just use ** instead of *
 
 '''
 
 
#==========unpacking list or tuple data to other variables dynamically=========
 
 
numbers = [1, 2, 3, 4, 5, 6]

# The left side of unpacking should be list or tuple.
a = numbers
# a = [1, 2, 3, 4, 5, 6]

*a, b = numbers
# a = [1, 2, 3, 4, 5]
# b = 6

a, *b = numbers
# a = 1 
# b = [2, 3, 4, 5, 6]

a, *b, c = numbers
# a = 1 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

























