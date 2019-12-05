from tkinter import *
root = Tk()


def my_click():

    # Working with Input
    hello = "Hello" + my_entry.get()
    # Both Work
    # my_label = Label(root, text="Hello " + my_entry.get())
    my_label = Label(root, text=hello)

    my_label.pack()


# Creating an input field
# my_entry = Entry(root)

# changing width
# my_entry = Entry(root, width=50)

# Changing color
# my_entry = Entry(root, width=50, bg="blue", fg="white")

# Changing border width (3D Effect)
# my_entry = Entry(root, width=50, borderwidth=5)

# Working with Input
my_entry = Entry(root, width=50)
my_entry.pack()
my_entry.insert(0, "Enter Your Name")


# my_button = Button(root, text="Enter Your Name", command=my_click)
my_button = Button(root, text="Enter Your Stock Quote", command=my_click)
my_button.pack()

root.mainloop()
