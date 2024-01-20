from tkinter import *

window = Tk()

frame = Frame(window, bg="light yellow", bd=5)
frame.pack(side= BOTTOM)

Button(frame, text="W", font=("Arial",25), width=3).pack(side = TOP)
Button(frame, text="A", font=("Arial",25), width=3).pack(side = LEFT)
Button(frame, text="S", font=("Arial",25), width=3).pack(side = LEFT)
Button(frame, text="D", font=("Arial",25), width=3).pack(side = LEFT)

window.mainloop()
