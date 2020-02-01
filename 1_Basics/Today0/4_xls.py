# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# pip install pyexcel_xls

from pyexcel_xls import save_data, read_data

data = {"sheet 1":[[1,2,3],[4,5,6],[4,5,6]], "sheet 2":[[2,3,'pavan'],['python','data']]}
save_data("myxls123.xls",data)

read_data = read_data("myxls123.xls")

print(read_data)