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


# Labels
header1 = Label(root,text="Temperature Converter",font=("Courier",15,"bold"), fg="black")
header2 = Label(root,text="Easily Convert Temperature For You",font=("Courier",10,"bold"), fg="black")
# Entry Box
# Grid
header1.grid(row=0,columnspan=2, sticky="WE",padx=60,pady=1)
header2.grid(row=1,columnspan=2, sticky="WE",padx=60,pady=0)
# Mainloop
root.mainloop()