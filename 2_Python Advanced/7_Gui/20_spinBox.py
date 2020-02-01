# -*- coding: utf-8 -*-
"""
Created on Thu May 31 23:55:56 2018

@author: SilverDoe
"""


from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0,row=0)
window.mainloop()