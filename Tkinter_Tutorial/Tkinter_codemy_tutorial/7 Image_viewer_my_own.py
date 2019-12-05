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

image_number_min = 6
image_number_max = 5


def forward(image_num):
    global my_label
    global button_forward
    global button_back
    global image_number_min
    global image_number_max

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number_min])
    my_label.grid(row=0, column=0, columnspan=3)

    image_num = image_num+1
    image_number_max = image_number_max + 1
    image_number_min = image_num

    if image_number_min == 7:
        button_forward = Button(root, text=">>", command=lambda: forward(image_number_min), state=DISABLED)
        button_forward.grid(row=1, column=2)

    if image_number_max > 0:
        button_back = Button(root, text="<<", command=lambda: back(image_number_max), state=NORMAL)
        button_back.grid(row=1, column=0)


def back(image_num):
    global my_label
    global button_back
    global image_number_max
    # global image_number_min
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number_max])
    my_label.grid(row=0, column=0, columnspan=3)
    image_num = image_num-1
    image_number_max = image_num
    if image_number_max == 0:
        button_back = Button(root, text="<<", command=lambda: back(image_number_max), state=DISABLED)
        button_back.grid(row=1, column=0)


button_back = Button(root, text="<<", command=back(image_number_max), state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(image_number_min))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
