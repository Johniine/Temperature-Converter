'''
Author: John
Purpose: To create a temperature calculator that is easy to use and accurate
Version 1: Created the Window
'''
# Import
from tkinter import *
# Files

# Class

# Functions

# Graphical User Interface
root = Tk()
root.geometry("380x270")
root.title("Temperature Converter")
# Make window non resisable and add an icon
root.resizable(0,0)
photo = PhotoImage(file="Icon.png")
root.iconphoto(False,photo)
# IntVar Entries
tempnum = IntVar()
# Set entry to ""
tempnum.set("")
# Labels
header1 = Label(root,text="Temperature Converter",font=("Courier",15,"bold"), fg="black",width=31)
header2 = Label(root,text="Easily Convert Temperature For You",font=("Courier",10,"bold"), fg="black")
# Entry Box
tempentry = Entry(root, textvariable=tempnum,font=("Courier",15,"bold"), fg="black",width=31,justify=CENTER)
# Grid
header1.grid(column=0,row=0,columnspan=1,padx=1,pady=0)
header2.grid(column=0,row=1,columnspan=2,padx=1,pady=0)
tempentry.grid(column=0,row=2,columnspan=2,padx=1,pady=0)
# Mainloop
root.mainloop()