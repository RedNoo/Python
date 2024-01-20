from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("420x420")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True, fill="both")

Label(tab1, text="Tab 1").pack()
Label(tab2, text="Tab 2").pack()

window.mainloop()
