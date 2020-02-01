# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:54:32 2018

@author: SilverDoe
"""

from tkinter import *

m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 1)

left = Entry(m1, bd = 5)
m1.add(left)

m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)

top = Scale( m2, orient = HORIZONTAL)
m2.add(top)

bottom = Button(m2, text = "OK")
m2.add(bottom)

mainloop()


#=============================  Methods  ======================================

'''
add(child, options) : Adds a child window to the paned window.

get(startindex [,endindex]) : This method returns a specific character or a range of text.


'''