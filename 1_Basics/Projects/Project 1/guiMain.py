# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:38:52 2018

@author: SilverDoe
"""

#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 26, 2018 11:37:06 AM

import sys
from tkinter import filedialog
from zipfile import BadZipfile
from FilterPyDocx import FilterPyDocx
from SimilarityFinder import SimilarityFinder
from TableBuilder import TableBuilder
from tkinter import messagebox

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True




class New_Toplevel:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI Black} -size 11 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"

        top = Tk()
        top.geometry("725x438+49+94")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
                      
        # get window width and height  
        w = 725 # width for the Tk root
        h = 438 # height for the Tk root
        
        # get screen width and height
        ws = top.winfo_screenwidth() # width of the screen
        hs = top.winfo_screenheight() # height of the screen
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        


        self.Label1 = Label(top)
        self.Label1.place(relx=0.11, rely=0.27, height=26, width=135)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Source Document :''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.11, rely=0.46, height=26, width=133)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Target Document :''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.11, rely=0.62, height=26, width=134)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''CSV save location :''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.36, rely=0.27,height=24, relwidth=0.28)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.36, rely=0.46,height=24, relwidth=0.28)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.36, rely=0.62,height=24, relwidth=0.28)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Button1 = Button(top,command=self.button1Command)
        self.Button1.place(relx=0.7, rely=0.25, height=33, width=96)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse''')
        self.Button1.configure(width=96)

        self.Button2 = Button(top,command=self.button2Command)
        self.Button2.place(relx=0.7, rely=0.43, height=33, width=96)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Browse''')
        self.Button2.configure(width=96)

        self.Button3 = Button(top,command=self.button3Command)
        self.Button3.place(relx=0.7, rely=0.59, height=33, width=96)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Browse''')
        self.Button3.configure(width=96)

        self.Button4 = Button(top,command=self.button4Command)
        self.Button4.place(relx=0.36, rely=0.82, height=33, width=196)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Execute''')
        self.Button4.configure(width=196)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.39, rely=0.07, height=26, width=162)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Similarity Finder''')
        self.Label4.configure(width=162)
        top.mainloop()
        
        
    def button1Command(self):
        path1 = filedialog.askopenfilename(initialdir="/",
                           filetypes =(("Document File", "*.docx"),("All Files","*.*")),
                           title = "Choose a file."
                           ) 
        try:
            self.Entry1.insert(0,path1)
            obj = FilterPyDocx(path1)
            self.slist1 = obj.extractSentences()
        except BadZipfile:
            messagebox.showinfo("Error", "BadZipFile : File is not a zip file")
        except FileNotFoundError:
            messagebox.showinfo("Error", "FileNotFoundError : No file selected")
            
        
    def button2Command(self):
        path2 = filedialog.askopenfilename(initialdir="/",
                           filetypes =(("Document File", "*.docx"),("All Files","*.*")),
                           title = "Choose a file."
                           )
        try:
            self.Entry2.insert(0,path2)
            obj2 = FilterPyDocx(path2)
            self.slist2 = obj2.extractSentences()
        except BadZipfile:
            messagebox.showinfo("Error", "BadZipFile : File is not a zip file")
        except FileNotFoundError:
            messagebox.showinfo("Error", "FileNotFoundError : No file selected")
        
        
    def button3Command(self):
        self.spath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        self.Entry3.insert(0,self.spath)
        #Using try in case user types in unknown file or closes without choosing a file.
        

    def button4Command(self):
        try:
            finder = SimilarityFinder(self.slist1,self.slist2);
            ratios,results= finder.ratres()
        
            data = {'Data1':self.slist1,'Data2':self.slist2,'Ratios':ratios,'Results':results}
            builder = TableBuilder(data)
            builder.generateCSV(self.spath)
        except IOError:
            messagebox.showinfo("Error", "IOError Occured : Failed to save...")
        except AttributeError:
            messagebox.showinfo("Error", "AttributeError Occured : Please select files to compare!")
        else:
            messagebox.showinfo("Message","CSV file generated!")
        


obj = New_Toplevel()







