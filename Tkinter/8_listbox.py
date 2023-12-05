from tkinter import *

window = Tk()

listbox = Listbox(window)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(1,"Hamburger")

window.mainloop()