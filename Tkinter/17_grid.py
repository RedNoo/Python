from tkinter import *

window = Tk()

firstname_label = Label(window, text="First Name").grid(row=0, column=0)
firstname_entry = Entry(window).grid(row=0, column=1)

lastname_label = Label(window, text="last Name").grid(row=1, column=0)
lastname_entry = Entry(window).grid(row=1, column=1)

window.mainloop()
