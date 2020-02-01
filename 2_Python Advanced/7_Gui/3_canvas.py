# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:58:01 2018

@author: SilverDoe
"""

"""  Canvas  """

from tkinter import *

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

C.pack()
top.mainloop()


""" ==========Canvas Options ==========
    bd : Border width in pixels. Default is 2
    bg : Normal background color.
    confine : If true (the default), the canvas cannot be scrolled outside of the scrollregion.
    cursor : Cursor used in the canvas like arrow, circle, dot etc.
    width : Size of the canvas in the X dimension.
    height : Size of the canvas in the Y dimension.
    highlightcolor : Color shown in the focus highlight.
    relief : Relief specifies the type of the border. Some of the values are SUNKEN, RAISED, GROOVE, and RIDGE.
    scrollregion : A tuple (w, n, e, s) that defines over how large an area the canvas can be scrolled, where w is the left side, n the top, e the right side, and s the bottom.
    xscrollincrement : If you set this option to some positive dimension, the canvas can be positioned only on multiples of that distance, and the value will be used for scrolling by scrolling units, such as when the user clicks on the arrows at the ends of a scrollbar.
    xscrollcommand : If the canvas is scrollable, this attribute should be the .set() method of the horizontal scrollbar
    yscrollincrement : Works like xscrollincrement, but governs vertical movement.
    yscrollcommand : If the canvas is scrollable, this attribute should be the .set() method of the vertical scrollbar.





"""


""" Canvas fill frame """

from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

C.pack(expand=YES, fill=BOTH) # size of the canvas fills the frame
top.mainloop()


""" Create arc """

from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

coord = 10, 50, 400, 210 # x0,y0,x1,y1
arc = C.create_arc(coord, start = 0, extent = 90, fill = "red")
C.pack()
top.mainloop()


""" create line """

from tkinter import *


top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

line = C.create_line(10,10,200,200,fill = 'white')
C.pack()
top.mainloop()


#   image

from tkinter import *


top = Tk()

C = Canvas(top, bg = "blue", height = 350, width = 600)

filename = PhotoImage(file = "D:\\Pictures\\ab60a380-ed80-0133-800b-0e31b36aeb7f.gif")
image = C.create_image(550, 30, anchor = NE, image = filename)
C.pack() # fixed canvas size
top.mainloop()

# Image resize 

from tkinter import *

# create the canvas, size in pixels
canvas = Canvas(width=600, height=350, bg='blue')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH) # size of the canvas fills the frame

# load the .gif image file
gif1 = PhotoImage(file='D:\\Pictures\\ab60a380-ed80-0133-800b-0e31b36aeb7f.gif')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor=NW)

# run it ...
mainloop()




# Scale image 
from PIL import Image, ImageTk
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()
w = 640
h = 500
cv = tk.Canvas(root, width=w, height=h,bg='blue')
cv.pack(fill='both', expand='yes')

# pick an image file you have .bmp  .jpg  .gif.  .png
# if not in the working directory, give full path
img_file = "D:\\Pictures\\ab60a380-ed80-0133-800b-0e31b36aeb7f.gif"
# open as a PIL image object
pil_image = Image.open(img_file)

# get the size of the original image
width_org, height_org = pil_image.size

# set the resizing factor so the aspect ratio is retained
# factor > 1.0 increases size
# factor < 1.0 decreases size

factor = 3 # Scaling factor
width = int(width_org * factor)
height = int(height_org * factor)
# use one of these filter options to resize the image:
# Image.NEAREST     use nearest neighbour
# Image.BILINEAR    linear interpolation in a 2x2 environment
# Image.BICUBIC     cubic spline interpolation in a 4x4 environment
# Image.ANTIALIAS   best down-sizing filter
pil_image2 = pil_image.resize((width, height), Image.ANTIALIAS)   

# optional title ...
sf = "{} ({}x{})".format(img_file, width, height)
root.title(sf)

# convert PIL image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(pil_image2)

# 'nw' uses upper left corner of the image as anchor
# image corner positions at canvas coordinates x=30, y=20
#cv.create_image(30, 20, image=tk_image, anchor='nw')

# 'center' is default --> uses center of picture
# at canvas coordinates x=250, y=250 (center of canvas)
cv.create_image(w//2, h//2, image=tk_image, anchor='center')

root.mainloop()


"""  Oval Shape   """

from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 420)

coord = 10, 50, 400, 210 # x0,y0,x1,y1
oval = C.create_oval(coord, fill = "red")
C.pack()
top.mainloop()

""" Polygon """

oval = canvas.create_polygon(x0, y0, x1, y1,...xn, yn, options)











