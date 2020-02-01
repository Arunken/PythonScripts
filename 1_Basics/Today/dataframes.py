# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:46:53 2018

@author: SilverDoe
"""

import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)



import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)


import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)


# Create a DataFrame from Dict of ndarrays / Lists

'''

All the ndarrays must be of same length. If index is passed, 
then the length of the index should equal to the length of the arrays.
If no index is passed, then by default, index will be range(n), where n is the array length
'''

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)


# create an indexed DataFrame using arrays

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)


# Create a DataFrame from List of Dicts

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)




# The following example shows how to create a DataFrame by passing a list of dictionaries and the row indices

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)



# The following example shows how to create a DataFrame with a list of dictionaries, row indices, and column indices

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)









































