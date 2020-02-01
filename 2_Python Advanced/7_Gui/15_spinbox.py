# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:48:23 2018

@author: SilverDoe
"""

from tkinter import *

master = Tk()

w = Spinbox(master, from_ = 0, to = 10)
w.pack()

mainloop()



from tkinter import *

root = Tk()
root.geometry('200x200+50+50')
root.title('Prueba')

t = ('One', 'Two', 'Three', 'Four', 'Five')
v = t[3]

var = StringVar()
var.set(v)
sb = Spinbox(root, values=t, textvariable=var, width=10)
sb.place(x=5, y=15)

root.mainloop()


#===========================  Methods  ========================================

'''
delete(startindex [,endindex]) : This method deletes a specific character or a range of text.

	
get(startindex [,endindex]) : This method returns a specific character or a range of text.

index(index) : Returns the absolute value of an index based on the given index.

insert(index [,string]...) : This method inserts strings at the specified index location.

invoke(element) : Invokes a spinbox button.

'''