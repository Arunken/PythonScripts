# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:41:52 2018

@author: SilverDoe
"""
'''
https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html

'''
import requests
from pprint import pprint
 
r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')
print(type(r.json())) # the received json data is a python dictionary
pprint(r.json())