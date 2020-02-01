# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:07:15 2018

@author: SilverDoe
"""

from tkinter import *

top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()



""" =====  options =========

command : A procedure to be called every time the user changes the state of this entry.

cursor : If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when
         it is over the entry.
         
image : To display a graphic image on the button.
highlightcolor : The color of the focus highlight when the checkbutton has the focus.

show : Normally, the characters that the user types appear in the entry. 
        To make a .password. entry that echoes each character as an asterisk, set show = "*"
        
state : The default is state = NORMAL, but you can use state = DISABLED to gray out the control and make it unresponsive.
         If the cursor is currently over the checkbutton, the state is ACTIVE
         
textvariable : In order to be able to retrieve the current text from your entry widget, 
                you must set this option to an instance of the StringVar class.

	
xscrollcommand : If you expect that users will often enter more text than the onscreen size of the widget,
                 you can link your entry widget to a scrollbar.

==== methods =====

delete ( first, last = None ) : Deletes characters from the widget, starting with the one at index first, 
                                up to but not including the character at position last. If the second argument is omitted, 
                                only the single character at position first is deleted.
                                
get() : Returns the entry's current text as a string.

	
icursor ( index ) : Set the insertion cursor just before the character at the given index.

insert ( index, s ) : Inserts string s before the character at the given index.



"""