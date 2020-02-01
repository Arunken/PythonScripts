# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:40:26 2018

@author: Arken
"""

print('I am line 1')
print('I am line 2')
print('I am line 3')

x = open('python_org.txt','r') # no such file exists and so an exception would be raised

print('I am line 4')
print('I am line 5')


# =============================================================================

x = int(input('enter a number : '))
y = int(input('enter a number : '))

try:
    z = x/y
    print(z)
    
except ZeroDivisionError as e:
    print('division by zero not possible')
    
# =============================================================================
    
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

number =10

while True:
    try:
        num = int(input("Enter a number"))
        if num<number:
            raise ValueTooSmallError
        elif num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("The value is too small, try again!")
    
    except ValueTooLargeError:
        print("This value is too large, try again!")
        
print("Congratulations ! you have guessed it correctly")


# =============================================================================


def name():
    pass
    print("hi") 
    
name()
