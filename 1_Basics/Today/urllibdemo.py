# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:36:39 2018

@author: SilverDoe
"""

try:
    from urllib2.request import urlopen # python 2.7
except:
    print("urllib2 doesn't exist")
    from urllib.request import urlopen


my_url = "https://wccftech.com"

fileurl = urlopen(my_url)

fileurl.read()

