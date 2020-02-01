# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:01:25 2018

@author: SilverDoe
"""

from  tkinter import *
root = Tk(  )
b = 0
for r in range(6):
    for c in range(6):
        b = b + 1
        Button(root, text = str(b),
            borderwidth = 1 ).grid(row = r,column = c)

root.mainloop()