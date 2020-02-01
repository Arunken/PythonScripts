# -*- coding: utf-8 -*-
"""
Created on Mon May 28 09:53:36 2018

@author: SilverDoe
"""

import requests
import re
from bs4 import BeautifulSoup

url = "http://www.wccftech.com"
req = requests.get(url)
soup = BeautifulSoup(req.content,"lxml")

data = soup.findAll({"title":True,"header":True,"description":True,"meta":True})

metatext = soup.find('meta',{"name":"description"})
type(metatext.get('content'))

    

    