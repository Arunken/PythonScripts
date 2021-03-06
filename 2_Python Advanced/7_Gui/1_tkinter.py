# -*- coding: utf-8 -*-
"""
Created on Tue May 22 09:37:38 2018

@author: SilverDoe
"""

# frame

import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()




# Position a frame

import tkinter as tk


root = tk.Tk() # create a Tk root window

w = 800 # width for the Tk root
h = 600 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen


# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop() # starts the mainloop