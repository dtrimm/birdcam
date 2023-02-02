
import tkinter
from tkinter import messagebox

top = tkinter.Tk()


# Code to add widgets will go here...

top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
B.flash()
top.mainloop()
