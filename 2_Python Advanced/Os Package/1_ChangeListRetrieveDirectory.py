# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 09:59:39 2018

@author: Kenrig
"""

import os

#================Retrieve current working directory (`cwd`)====================
cwd = os.getcwd()
print(cwd)

# Change directory 
os.chdir("/home/arken/trashdata")
print(os.getcwd())

# ==============List all files and directories in current directory============
ldir = os.listdir('.')
print(ldir)

# =============== creates a directory =========================================
import os

# Create a directory "test"
os.mkdir("test")

# ============== change the current directory =================================
import os

# Changing a directory to "/test"
os.chdir("test")

# ============ renaming a file ================================================

import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# ============ deleting a directory ===========================================

import os

# This would  remove "/ttt"  directory.
os.rmdir( "test"  )










