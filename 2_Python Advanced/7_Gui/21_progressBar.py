# -*- coding: utf-8 -*-
"""
Created on Thu May 31 23:57:18 2018

@author: SilverDoe
"""


from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=0)
window.mainloop()