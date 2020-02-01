# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:18:10 2018

@author: SilverDoe
"""

from tkinter import *

import tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Calicut")
Lb1.insert(2, "Chennai")
Lb1.insert(3, "Bangalore")
Lb1.insert(4, "Mumbai")


Lb1.pack()
top.mainloop()


#=========================  Options  ==========================================
'''
	
selectmode : Determines how many items can be selected, and how mouse drags affect the selection

            1) BROWSE − Normally, you can only select one line out of a listbox. If you click on an item and then drag to a different line,
                 the selection will follow the mouse. This is the default.
                 
            2) SINGLE − You can only select one line, and you can't drag the mouse.wherever you click button 1, that line is selected.

            3) MULTIPLE − You can select any number of lines at once. Clicking on any line toggles whether or not it is selected.

            4) EXTENDED − You can select any adjacent group of lines at once by clicking on the first line and dragging to the last line.



'''

#=======================  Methods  ============================================

'''

activate ( index ) : Selects the line specifies by the given index.

curselection() : Returns a tuple containing the line numbers of the selected element or elements,
                 counting from 0. If nothing is selected, returns an empty tuple.
                 
delete ( first, last = None ) : Deletes the lines whose indices are in the range [first, last].
                                 If the second argument is omitted, the single line with index first is deleted.
                                 
         
get ( first, last = None ) : Returns a tuple containing the text of the lines with indices from first to last, 
                            inclusive. If the second argument is omitted, returns the text of the line closest to first.       
                
index ( i ) : If possible, positions the visible part of the listbox so that the line containing index i is at the top of the widget.

insert ( index, *elements ) : Insert one or more new lines into the listbox before the line specified by index. 
                                Use END as the first argument if you want to add new lines to the end of the listbox.
                                
see ( index ) : Adjust the position of the listbox so that the line referred to by index is visible.                                
                                
size() : Returns the number of lines in the listbox.                    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

'''