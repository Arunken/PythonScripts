# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:57:24 2018

@author: SilverDoe
"""

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()