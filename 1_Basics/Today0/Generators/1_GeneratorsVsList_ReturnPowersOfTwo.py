# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:40:33 2018

@author: Ourabora
"""

#=================LIST====================

# First, we define a list
the_list = [2**x for x in range(5)]

# Type check: yes, it's a list
type(the_list)


# Iterate over items and print them
for element in the_list:
    print(element)
    
# How about the length?
len(the_list)    
    
#==============GENERATORS================
    

# Ok, now a generator.
# As easy as list comprehensions, but with '()' instead of '[]':
the_generator = (2**x for x in range(5))

# Type check: yes, it's a generator
type(the_generator)

# Iterate over items and print them
for element in the_generator:
    print(element)

next(the_generator)    

# Everything looks the same, but the length...
len(the_generator) # TypeError: object of type 'generator' has no len()
    
    
# Generator to search for some keyword in a huge text file line-by-line 

def search(keyword, filename):
    print('generator started')
    
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()

fp = '/mnt/Soft/Documents/PythonProjects/1_Basics/DataForFiles/file2.txt'
the_generator = search('Sam', fp) 
                        # When we call the search function, its body code does not run. 
                        # The generator function will only return the generator object, acting as a constructor

type(search) #<class 'function'>
type(the_generator) #<class 'generator'>

print(next(the_generator)) # Iterate
                           # We got the first search result without looking through the whole file

    
    
    
    
    
    