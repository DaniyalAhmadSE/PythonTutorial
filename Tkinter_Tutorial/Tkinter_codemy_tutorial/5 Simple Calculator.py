from tkinter import *

root = Tk()
root.title("Simple Calculator")

# not in tutorial just to remove error
f_num = 0

my_entry = Entry(root, width=35, borderwidth=5)
my_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# my_entry.insert(0, "")


def button_click(number):
    # my_entry.delete(0, END)
    current = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, str(current) + str(number))


def clear():
    my_entry.delete(0, END)


def add():
    first_number = my_entry.get()
    global f_num
    f_num = int(first_number)
    my_entry.delete(0, END)


def equal():
    second_number = my_entry.get()
    my_entry.delete(0, END)
    my_entry.insert(0, f_num + int(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear)

# Put the Buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
