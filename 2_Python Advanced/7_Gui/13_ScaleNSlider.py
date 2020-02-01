# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:40:42 2018

@author: SilverDoe
"""
#==========================  Scale  =============================================
from tkinter import *

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor = CENTER)

button = Button(root, text = "Get Scale Value", command = sel)
button.pack(anchor = CENTER)

label = Label(root)
label.pack()

root.mainloop()



''' ===================  Methods  =============================================

get() : 	This method returns the current value of the scale.

set ( value ) : 	Sets the scale's value.

'''


#============================  Scrollbar  =====================================

from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()



'''

get() : Returns two numbers (a, b) describing the current position of the slider. The a 
        value gives the position of the left or top edge of the slider, for horizontal and
        vertical scrollbars respectively; the b value gives the position of the right or bottom edge
        
set ( first, last ) : To connect a scrollbar to another widget w, set w's xscrollcommand or 
                      yscrollcommand to the scrollbar's set() method. The arguments have the same meaning as the
                      values returned by the get() method.

'''