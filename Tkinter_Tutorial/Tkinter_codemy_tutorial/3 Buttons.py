from tkinter import *
root = Tk()


def my_click():
    my_label = Label(root, text="Look! I clicked a Button!!")
    my_label.pack()


# # Creating a button
# my_button = Button(root, text="Click Me!")

# # To make button disabled
# my_button = Button(root, text="Click Me!", state=DISABLED)

# # resizing a button
# my_button = Button(root, text="Click Me!", padx=0, pady=50)

# # giving a link
# my_button = Button(root, text="Click Me!", command=my_click)

# # changing the colour
my_button = Button(root, text="Click Me!", command=my_click,
                   fg="#FFDAB9", bg="#8A2BE2")

my_button.pack()
root.mainloop()
