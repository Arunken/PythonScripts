# -*- coding: utf-8 -*-
"""
Created on Tue May 22 09:43:26 2018

@author: SilverDoe
"""

# Add button

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Click", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()