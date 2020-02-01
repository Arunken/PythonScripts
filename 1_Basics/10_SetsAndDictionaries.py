# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:57:07 2018

@author: Ourabora
"""

li = [1,2,1,2] # list
tu = (1,2,1,2) # tuple
se = {1,2,1,2} # set >> wont be shown in variable explorer as it is not indexed
dic = {'a':1,'b':2,'c':3,'d':4} # dictionary


# ================= Sets ======================================================

# In a list and a tuple duplicate values are allowed.
# Sets do not support duplicate values. Duplicates will be removed.
# Lists/Tuples are ordered(indexed).
# Sets and dictionaries are not ordered(not indexed)
# Sets are not iterable as they do not have indexes.
# Sets are the same as in mathematics.

# =============================================================================

# Operations on sets :

a = {1,'arun',2,'ken',2}
a.add("user")
b = {1,2,'python','programming'}
print(a)


c = a|b # OR
d = a&b # AND
e = a-b # Only in a
f = b-a # Only in b
g = a^b # XOR

print(c)
print(d)
print(e)
print(f)
print(g)


# Sets can be used for removing duplicates from a list and sort it :

mylis = [1,2,1,3,8,55,6,5,2]

newsetlis = list(set(mylis))



# ================= Dictionaries ==============================================

# Unordered mutable collection of mapping objects.
# Values accessed by key.
# Heterogenous.
# Can be nested.
# Can vary in size.
# Modifiable in place.
# Hash table based for efficiency.
# d ={} creates an empty dictionary.

# =============================================================================

dic1 = {'name':"Arun",'age':26,'roll no':16}
dic1['name']
#(name':"Arun",'age':26,'roll no':16) creates a dictionary from the key value pairs

myname =dic1['name'] # return the corresponding value for the given key
dic1['name'] = "Goku" # Change the value for the given key
newname = dic1['name']  
dic1['city'] = "Calicut" # Adds a new key-value pair if the key doesn't exist

length = len(dic1)
# dic1.clear() # empties the dictionary

# Dictionary Operations :

records = {'Arun':4,'Goku':44,'Naruto':2,'Hinata':1,'Sasi':7}

if 'Arun' in records: # Checks the existence of a key in the dictionary
    print('information regarding Arun is present in the record')
    
else:
    print('information regarding Arun is not present in the record')
    
    
del records['Arun'] # deletes the key 'Arun'
records.pop('Goku') # removes and returns the value of key 'Goku'
records.pop('Naruto',0) # removes/returns value of 'Naruto' else 0
records.get('Hinata','nil') # gives value of 'Hinata' else 'nil'
records.setdefault('Sasi',5) # if exists, return value else create/return new

minirecord = {'Sasi':34,'amaterasu':87}
records.update(minirecord) # updates records, samekeys upddated, new added

keys = records.keys() # returns an iterable of keys
print(keys)
print(type(keys))
values = records.values() # returns an iterable of values
print(values)
print(type(values))

lkeys = list(keys) # makes a list of keys
lvalues = list(values) # makes alist of values

tupleItems = records.items() # returns an iterable of key, value tuples
print(tupleItems)
type(tupleItems)

# Using key, value in iteration :

for k,v in tupleItems:
    print('key : ',k)
    print('value : ',v)
    
# Dictionary & Lists :    
     
lisdi = ['Arun',{'eng':89,'math':76,'phy':80},'delhi'] # a list accomodating a dictionary
print(lisdi[1]['eng'])


dicli = {'roll':142,'marks':[70,89,56,65],'city':'delhi'} # a dictionary accomodating a list
print(dicli['marks'][2]) 


 # creating a zip from keys-values and create a dictionary from the zip
 
labdict = {'Arun':23,'David':87,'Gabriel':75}
labkeys = labdict.keys()
labvalues = labdict.values()
print('keys : ',labkeys)
print('values : ',labvalues)
labzip = zip(labkeys,labvalues) # creates a zip from the keys and values
zipdict = dict(labzip) # creates a dictionary from the zip  
print('zip : ',labzip)
print('new dictionary : ',labdict)











