'''
Author: John
Purpose: To create a temperature calculator that is easy to use and accurate
Version 1: Created the Window
'''
# Import
from tkinter import *
# Files

# Colours
fg_colour = 'black'
cel_bg_colour = 'skyblue'
far_bg_colour = 'orange'
help_bg_colour = '#990099'
hist_bg_colour = '#009900'

# Fonts
btn_fonts = ("Courier",15,"bold")

# Class
class Converter:
    def __init__(self) -> None:
        # Set Up The Graphical User Interface
        # Errors
        error1 = 'Please enter a number'
        # IntVar Entries
        self.tempnum = IntVar()
        # Set entry to ""
        self.tempnum.set("")
        # Labels
        self.header1 = Label(root,text="Temperature Converter",font=btn_fonts, fg=fg_colour,width=31)
        self.header2 = Label(root,text="Easily Convert Temperature For You",font=("Courier",10,"bold"), fg=fg_colour)
        self.conv_label = Label(root,text="",font=("Courier",10,"bold"), fg=fg_colour,justify=CENTER,bg="#FCF55F",width=46,height=2)
        self.error_label = Label(root,text="",font=("Courier",10,"bold"), fg=fg_colour,justify=CENTER,width=46,height=2)
        # Entry Box
        self.tempentry = Entry(root, textvariable=self.tempnum,font=btn_fonts, fg=fg_colour,width=31,justify=CENTER)
        # Buttons
        self.celsius_but = Button(root,text="Celsius",font=btn_fonts,fg=fg_colour,bg=cel_bg_colour,width=14,command=self.to_celsius)
        self.faren_but = Button(root,text="Farenhiet",font=btn_fonts,fg=fg_colour,bg=far_bg_colour,width=14)
        self.help_but = Button(root,text="Help/Info",font=btn_fonts,fg=fg_colour,bg=help_bg_colour,width=14)
        self.hist_but = Button(root,text="History",font=btn_fonts,fg=fg_colour,bg=hist_bg_colour,width=14,state=DISABLED) 
        # Grid
        self.header1.grid(column=0,row=0,padx=1,pady=0,columnspan=2)
        self.header2.grid(column=0,row=1,padx=1,pady=0,columnspan=2)
        self.tempentry.grid(column=0,row=2,padx=1,pady=0,columnspan=2)
        self.conv_label.grid(column=0,row=3,padx=1,pady=5,columnspan=2)
        self.error_label.grid(column=0,row=4,padx=1,pady=2,columnspan=2)
        self.celsius_but.grid(column=0,row=5,padx=0,pady=5,sticky="WE")
        self.faren_but.grid(column=1,row=5,padx=0,pady=5,sticky="WE")
        self.help_but.grid(column=0,row=6,padx=0,pady=0,sticky="WE")
        self.hist_but.grid(column=1,row=6,padx=0,pady=0,sticky="WE")
        # Methods
    def check_temp(self,min_value):
        '''This function check if input entered is a minimumn value to 0'''
        error0 = f'Please enter a number that is more than {min_value}'

        try:
            response = self.tempnum.get()
            if response < min_value:
                print(error0)
            else:
                return response
        except ValueError:
            print(error0)
    
    def to_celsius(self):
        self.check_temp(-459)

        
# Mainloop
if __name__ == '__main__':
    root = Tk()
    root.geometry("380x270")
    root.title("Temperature Converter")
    root.resizable(0,0)
    photo = PhotoImage(file="Icon.png")
    root.iconphoto(False,photo)
    Converter()
    root.mainloop()