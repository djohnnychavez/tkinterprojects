from tkinter import *
from PIL import ImageTk,Image 

root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap(r'C:\Users\Bug\Pictures\2998124-bug-ladybird-ladybug-virus_99843.ico')

#the image you open is subject to change
my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Bug\Pictures\bugs.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\Bug\Pictures\bugs2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\Bug\Pictures\bugs3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\Bug\Pictures\bugs4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\Bug\Pictures\bugs5.jpg"))
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward= Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward= Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


#these are my buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)









root.mainloop()
