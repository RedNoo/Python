from tkinter import *

def open_file():
    print("open file")

def save_file():
    print("save file")





window = Tk()

sample_image = PhotoImage(file="warehouse.png")

menubar = Menu(window)

window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=sample_image,compound="left")
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)


edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

window.mainloop()
