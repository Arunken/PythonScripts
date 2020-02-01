# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 00:00:33 2018

@author: SilverDoe
"""


from tkinter import filedialog

file = filedialog.askopenfilename()
print(file)
#file = filedialog.askopenfilenames()
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
#dir = filedialog.askdirectory()

spath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpg files","*.jpg"),("all files","*.*")))