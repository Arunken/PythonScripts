# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:25:00 2018

@author: SilverDoe
"""

# read from a file containing a url in each line and create a list of domains from it

# Eg : if url is http://www.niit.com/training.html then domain is www.niit.com

f_in = open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\file3.txt','r')
urls = f_in.readlines() # Returns a list with each element as a line from the file
domains=[]
for i in urls:
    domain=i.split("//")[-1].split("/")[0].split('?')[0]
    if domain not in domains:
        domains.append(domain)
        
print(domains)
f_in.close()



