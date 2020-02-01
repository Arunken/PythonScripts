# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:29:21 2018

@author: SilverDoe
"""

from tkinter import *

import tkinter

top = Tk()

mb =  Menubutton ( top, text = "condiments", relief = RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label = "mayo",
                          variable = mayoVar )
mb.menu.add_checkbutton ( label = "ketchup",
                          variable = ketchVar )

mb.pack()
top.mainloop()