# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:43:19 2018

@author: SilverDoe
"""

# program to find sequences of lowercase letters joined with a underscore

import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))



# Write Python program to search the numbers (0-9) of length between 1 to 2 in a given string.
import re

s = "Exercises number 1, 12, 13, and 345 are important"
results = re.finditer(r"([0-9]{1,2})", s)
print("Number of length 1 to 2")
for num in results:
     print(num.group(0))
     
     
# Ask the user to enter a number until they guess a stored number correctly

class Error(Exception):
    pass

class ValueTooSmallError(Error):
        pass

class ValueTooLargeError(Error):
        pass

number =10

while True:
    try:
        num = int(input("Enter a number : "))
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


# Matches a string that has an a followed by zero or more b's

import re
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
print(text_match("abbb"))
print(text_match("abbbb"))


# Input a filename from the user. Load the text from this file if this file exists, otherwise the text should be blank

import os.path

fpath = 'E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\file1.txt'
if os.path.isfile(fpath):
    f_in = open(fpath,'r')
    text = f_in.read()
    print(text)
    f_in.close()
else:
    pass
    

# Take a input from user and display reciprocal of it.
    
class Error(Exception):
    pass

class NumberFormatError(Error):
        pass

class DivideByZeroError(Error):
        pass
    

try:
    snumb = input("Enter a number : ")
    if not snumb.isdigit():
        raise NumberFormatError
    elif int(snumb)==0:
        raise DivideByZeroError

    numb = int(snumb)
    rec = 1/numb
    print("Reciprocal is : ",rec)
    
except NumberFormatError:
    print("Please enter a number")
except DivideByZeroError:
    print("Division by zero is infinite, Please enter a non-zero value!")
except Exception:
    print("Exception occured : Input cannot be processed")
    
    
    
# a regex in Python, how can I verify that a user's password is:

    #At least 8 characters
    #uppercase letters: A-Z
    #lowercase letters: a-z
    #numbers: 0-9
    #any of the special characters: $#@
    

import re

def validate(pwds):
    for pwd in pwds:
        if re.match(r'[A-Za-z0-9$#@]{6,12}', pwd):
           print(pwd)            
        else:
            pass
        
s = input('Enter passwords separated by commas')
s1 = "ABd1234@1,aF1#2w3E*,2We3345"
pwds = s1.split(",")
validate(pwds)

    





























