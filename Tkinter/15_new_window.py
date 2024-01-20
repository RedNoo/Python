from tkinter import *


def create_window():
    new_window = Tk()  # Toplevel()
    old_window.destroy()


old_window = Tk()

Button(old_window, text="create window", command=create_window).pack()

old_window.mainloop()
