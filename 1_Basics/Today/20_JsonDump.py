# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:25:56 2018

@author: Ourabora
"""

import json


# Dictionary

d = {'101':'Arun','102':'Deepak','104':'Anuradha'} # dictionary data

jsonStr = json.dumps(d) # Dumps the dictionary into a json string
print(jsonStr)

nd = json.loads(jsonStr) # loads the data from the json string as a dictionary type


# List

li = [10,30,40,50] # List data
dmp = json.dumps(li) # Dumps the list into a json string

"""
=============================Python to JSON conversion=========================

Python              JSON
------              -----
Dictionary          Object
List, Tuple         Array
Str                 string
int,float           number
True                true
False               false
None                null

===============================================================================

"""

