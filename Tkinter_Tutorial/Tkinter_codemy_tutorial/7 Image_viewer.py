from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hi')
root.iconbitmap('Images/Icons/cal.ico')


my_img1 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/Hi.png'))
my_img2 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/a.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/b.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/c.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/d.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/e.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('Images/Image_viewer_images/f.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]


my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_num):
    global my_label
    global button_forward
    global button_back


button_back = Button(root, text="<<", command=back(0))
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
