# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:59:43 2018

@author: SilverDoe
"""

from tkinter import *

    
top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
top.mainloop()


""" =====  options =========

command : A procedure to be called every time the user changes the state of this checkbutton.
cursor : If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.
image : To display a graphic image on the button.

==== methods =====

deselect() : Clears (turns off) the checkbutton.
flash() : Flashes the checkbutton a few times between its active and normal colors, but leaves it the way it started.
invoke() : You can call this method to get the same actions that would occur if the user clicked on the checkbutton to change its state.
select() : Sets (turns on) the checkbutton.
toggle() : Clears the checkbutton if set, sets it if cleared.

"""