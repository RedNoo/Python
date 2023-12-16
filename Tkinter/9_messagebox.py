from tkinter import *
from tkinter import messagebox


def click():
    #messagebox.showinfo(title="this is title", message="this is message")
    #messagebox.showerror(title="this is title", message="this is message")
    #messagebox.showwarning(title="this is title", message="this is message")

    if messagebox.askokcancel(title="Ask ok cancel?",message="do you really want to do this?",icon="info"):
        print("ok")
    else:
        print("cancel")

    #messagebox.askretrycancel()
    #messagebox.askyesno()

window = Tk()

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()