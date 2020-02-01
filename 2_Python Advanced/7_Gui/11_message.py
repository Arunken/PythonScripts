# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:34:09 2018

@author: SilverDoe
"""

from tkinter import *

root = Tk()

var = StringVar()
label = Message( root, textvariable = var, relief = RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()