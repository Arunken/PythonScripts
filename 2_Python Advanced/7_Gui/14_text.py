# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:46:55 2018

@author: SilverDoe
"""

from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")
root.mainloop()