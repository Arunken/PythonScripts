# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:17:01 2018

@author: SilverDoe
"""

"""
The Frame widget is very important for the process of grouping and organizing other widgets in a somehow friendly way.
 It works like a container, which is responsible for arranging the position of other widgets
"""

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Red", fg = "red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text = "Black", fg = "black")
blackbutton.pack( side = BOTTOM)

root.mainloop()