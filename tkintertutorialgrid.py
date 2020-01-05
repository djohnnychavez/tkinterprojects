from tkinter import *

root = Tk()

# Creating a label widget
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Bug!")
# Shoving it onto a screen

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()