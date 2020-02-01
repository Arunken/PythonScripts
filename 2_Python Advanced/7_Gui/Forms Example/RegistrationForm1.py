# -*- coding: utf-8 -*-
"""
Created on Thu May 31 23:16:36 2018

@author: SilverDoe
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox



class MyGui:
    



    def __init__(self):
        window = Tk()
        window.title("Welcome to LikeGeeks app")
        window.geometry('400x600')
        
        lbl = Label(window, text="Name : ")
        lbl.grid(column=0, row=0)
        
        self.txtvar = StringVar()
        self.txt = Entry(window,width=10,textvariable=self.txtvar) #state='disabled'
        self.txt.grid(column=1, row=0)
        self.txt.focus()
        
        lbl = Label(window, text="City : ")
        lbl.grid(column=0, row=1)
        
        self.combo = Combobox(window)
        self.combo['values']= ('-select-','Bangalore','Calicut', 'Chennai', 'Pune', 'Mumbai')
        self.combo.current(0) #set the selected item
        self.combo.grid(column=1, row=1)
        
        lbl = Label(window, text="Options : ")
        lbl.grid(column=0, row=2)
        
        self.chk_state1 = BooleanVar()
        self.chk_state1.set(True) #set check state
        self.chk1 = Checkbutton(window, text='Choose1', var=self.chk_state1)
        self.chk1.grid(column=1, row=2)
        #chk_state.set(0) #uncheck
        #chk_state.set(1) #check
        
        self.chk_state2 = BooleanVar()
        self.chk_state2.set(True) #set check state
        self.chk2 = Checkbutton(window, text='Choose2', var=self.chk_state2)
        self.chk2.grid(column=2, row=2)
        
        lbl = Label(window, text="Gender : ")
        lbl.grid(column=0, row=3)
        
        self.radvar = IntVar()
        self.rad1 = Radiobutton(window,text='Male', value=1, variable=self.radvar)
        self.rad2 = Radiobutton(window,text='Female', value=2, variable=self.radvar)
        self.rad1.grid(column=1, row=3)
        self.rad2.grid(column=2, row=3)
        
        lbl = Label(window, text="Address : ")
        lbl.grid(column=0, row=4)
        
        self.txtaddr = scrolledtext.ScrolledText(window,width=30,height=10)
        self.txtaddr.grid(column=1,row=4)
        #txt.insert(INSERT,'You text goes here')
        #txt.delete(1.0,END)
        
        lbl = Label(window, text="Password : ")
        lbl.grid(column=0, row=5)
        
        self.txtpassvar = StringVar()
        self.txtpass = Entry(window,width=10,textvariable=self.txtpassvar, show="*") #state='disabled'
        self.txtpass.grid(column=1, row=5)
        
        
        btn = Button(window, text="Click Me", command=self.btnAction)
        btn.grid(column=1, row=6)
        
        window.mainloop()
        
    def btnAction(self):
        #messagebox.showinfo("Say Hello", "Hello World")
        #messagebox.showwarning('Message title', 'Message content')  #shows warning message
        #messagebox.showerror('Message title', 'Message content')    #shows error message
        uname = self.txtvar.get()
        city = self.combo.get()
        
        gender = ''
        if self.radvar.get()==1:
            gender = self.rad1.cget('text')
        elif self.radvar.get()==2:
            gender = self.rad2.cget('text')
        
        options = ''
        if self.chk_state1.get()==True:
            options = options+self.chk1.cget("text")
        if self.chk_state2.get()==True: 
            options = options+self.chk2.cget("text")
            
        address = self.txtaddr.get(1.0, END)
        
        password = self.txtpassvar.get()
        
        print(uname)
        print(city)
        print(gender)
        print(options)
        print(address)
        print(password)
        
        


obj = MyGui()

