from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap(r'C:\Users\Bug\Pictures\2998124-bug-ladybird-ladybug-virus_99843.ico')

my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Bug\Pictures\bugs.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()

root.mainloop()
