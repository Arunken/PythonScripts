# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:14:50 2018

@author: Kenrig
"""

# 1) ================= Write a Python program that matches a string that has an a followed by zero or more b's.

import re

def search_match(s):
        pattern = 'ab*?b'
        if re.search(pattern,  s):
                return 'matched!'
        else:
                return('Not matched!')


print(search_match("ab"))
print(search_match("abb"))
print(search_match("abbc"))