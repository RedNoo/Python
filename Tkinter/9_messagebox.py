from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo(title="this is title", message="this is message")

window = Tk()

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()