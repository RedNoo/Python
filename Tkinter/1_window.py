from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("this is the window title")
icon = PhotoImage(file="warehouse.png")
window.iconphoto(True,icon)
window.config(background="#515151")

window.mainloop()

