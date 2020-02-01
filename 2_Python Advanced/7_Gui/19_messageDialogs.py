# -*- coding: utf-8 -*-
"""
Created on Thu May 31 23:54:45 2018

@author: SilverDoe
"""


from tkinter import messagebox
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')