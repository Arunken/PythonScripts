# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:55:47 2018

@author: SilverDoe
"""
'''=========================== JSON(javascript Object Notation) ===========================================

>> JSON is an open-standard file format that uses human-readable text to transmit
 data objects consisting of attribute–value pairs and array data types(or any other serializable value).
 
>> JSON  is a very common data format used for asynchronous browser/server communication. 
'''


'''======================= JSON DUMPS ========================================='''
import json

str_data = 'normal string'
int_data = 1
float_data = 1.50
list_data = [str_data, int_data, float_data]
nested_list = [int_data, float_data, list_data]
dictionary = {'int': int_data,'str': str_data,'float': float_data,'list': list_data,'nested list': nested_list}

jsonstr = json.dumps(str_data)
jsonint = json.dumps(int_data)
jsonfloat = json.dumps(float_data)
jsonlist = json.dumps(list_data)
jsonnested = json.dumps(nested_list, indent=2)
jsondict = json.dumps(dictionary, indent=2)

type(jsonstr)

# convert them to JSON data and then print it
print('String :', jsonstr)
print('Integer :', jsonint)
print('Float :', jsonfloat)
print('List :', jsonlist)
print('Nested List :', jsonnested)
print('Dictionary :', jsondict)  # the json data will be indented

'''========================= JSON LOADS ======================================='''

str_data = json.loads(jsonstr)
int_data = json.loads(jsonint)
float_data = json.loads(jsonfloat)
list_data = json.loads(jsonlist)
nested_list = json.loads(jsonnested)
dictionary = json.loads(jsondict)

type(str_data)
type(int_data)
type(float_data)
type(list_data)
type(nested_list)
type(dictionary)






















