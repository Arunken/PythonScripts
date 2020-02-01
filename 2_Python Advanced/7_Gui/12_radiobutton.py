# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:36:01 2018

@author: SilverDoe
"""

from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text = "Option 1", variable = var, value = 1,
                  command = sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text = "Option 2", variable = var, value = 2,
                  command = sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text = "Option 3", variable = var, value = 3,
                  command = sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()


#============================  Methods  =======================================

'''

deselect() : Clears (turns off) the radiobutton.

flash() : Flashes the radiobutton a few times between its active and normal colors, but leaves it the way it started.

invoke() : You can call this method to get the same actions that would occur if the user clicked on the radiobutton to change its state.

select() : Sets (turns on) the radiobutton

'''




