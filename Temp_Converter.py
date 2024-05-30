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
#root.resizable(0,0)
photo = PhotoImage(file="Icon.png")
root.iconphoto(False,photo)
# IntVar Entries
tempnum = IntVar()
# Set entry to ""
tempnum.set("")
# Labels
header1 = Label(root,text="Temperature Converter",font=("Courier",15,"bold"), fg="black",width=31)
header2 = Label(root,text="Easily Convert Temperature For You",font=("Courier",10,"bold"), fg="black")
conv_label = Label(root,text="",font=("Courier",10,"bold"), fg="black",justify=CENTER,bg="#FCF55F",width=46)
error_label = Label(root,text="",font=("Courier",10,"bold"), fg="black",justify=CENTER,bg="#FF4433",width=46)
# Entry Box
tempentry = Entry(root, textvariable=tempnum,font=("Courier",15,"bold"), fg="black",width=31,justify=CENTER)
# Buttons
celsius_but = Button(root,text="Celsius",font=("Courier",15,"bold"),fg='black',bg="skyblue",width=14)
faren_but = Button(root,text="Farenhiet",font=("Courier",15,"bold"),fg='black',bg="orange",width=14)
help_but = Button(root,text="Help/Info",font=("Courier",15,"bold"),fg='black',bg="purple",width=14)
hist_but = Button(root,text="History",font=("Courier",15,"bold"),fg='black',bg="green",width=14)
# Grid
header1.grid(column=0,row=0,padx=1,pady=0,columnspan=2)
header2.grid(column=0,row=1,padx=1,pady=0,columnspan=2)
tempentry.grid(column=0,row=2,padx=1,pady=0,columnspan=2)
conv_label.grid(column=0,row=3,padx=1,pady=5,columnspan=2)
error_label.grid(column=0,row=4,padx=1,pady=2,columnspan=2)
celsius_but.grid(column=0,row=5,padx=0,pady=5,sticky="WE")
faren_but.grid(column=1,row=5,padx=0,pady=5,sticky="WE")
help_but.grid(column=0,row=6,padx=0,pady=0,sticky="WE")
hist_but.grid(column=1,row=6,padx=0,pady=0,sticky="WE")
# Mainloop
root.mainloop()