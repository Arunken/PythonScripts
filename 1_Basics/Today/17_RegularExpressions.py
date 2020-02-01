# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:55:45 2018

@author: Ourabora
"""

import re


# ====================== Difference between match and search===================

# Match

pattern = re.compile('A..T') # starts with A and ends with T and two characters in between
matchobject = pattern.match('ACGTAAT') # Will match a pattern if it is contained in the start of the string
if matchobject:
    print('Matched string :',matchobject.group()) # displays 'ACGT'
    print(matchobject.start(),matchobject.end()) # start and ending index of the matched pattern
else:
    print("No match found")


# Search
    
pattern = re.compile('T..T') # starts with A and ends with T and two characters in between
matchobject = pattern.search('ACGTAAT') # Will match a pattern if contained anywhere in the string
if matchobject:
    print('Matched string :',matchobject.group()) # displays 'ACGT'
    print(matchobject.start(),matchobject.end()) # start and ending index of the matched pattern
else:
    print("No match found")
    

"""
 =================================Metacharacters===============================
 
 .      matches any one character except \n
 \w     matches any alphanumeric character
 \W     matches any non-alphanumeric character
 \d     matches any digit
 \D     matches any non digit
 \s     matches any white space character
 \S     matches any non white space character
 
 []     any one character from this set
 [AT]   means either A or T is matched
 [A-G]  matches any character between A to G
 [^AT]  matches any character except from this set
 ()     used for grouping expressions
 |      for using or condition
 \      for negating meaning of metacharacter
 
 ^ match in the beginning of the string
 $ match at end of the string
 * Zero or more occurence of previous character
 + One or moreoccurence of previous character
 ? Zero or one occurence of previous character
 {m,n} minimum m occurences and maximum n occurence 

"""


import re 

pattern =re.compile('\d[A-Z]') # matches any one character

matchobject = pattern.match('ASAATST')
if(matchobject): # if match was found
    print(matchobject.group()) # displays 'ACGT'
    print(matchobject.start(),matchobject.end())
    
    
