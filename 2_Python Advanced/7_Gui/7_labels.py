# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:15:52 2018

@author: SilverDoe
"""

from tkinter import *

root = Tk()

var = StringVar()
label = Label( root, textvariable = var, relief = RAISED )

var.set("Hello there!!!")
label.pack()
root.mainloop()


