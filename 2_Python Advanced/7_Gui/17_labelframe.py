# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:56:31 2018

@author: SilverDoe
"""

from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text = "This is a LabelFrame")
labelframe.pack(fill = "both", expand = "yes")
 
left = Label(labelframe, text = "Inside the LabelFrame")
left.pack()
 
root.mainloop()