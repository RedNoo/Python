from tkinter import *


def move_up(event):
    canvas.move(myimage,0,-10)


def move_down(event):
    canvas.move(myimage,0,10)


def move_left(event):
    canvas.move(myimage,-10,0)


def move_right(event):
    canvas.move(myimage,10,0)


window = Tk()
canvas = Canvas(window, width=500, height=500)
canvas.pack()

window.bind("<w>", move_up)
window.bind("<Up>", move_up)
window.bind("<s>", move_down)
window.bind("<Down>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

photoimage = PhotoImage(file="warehouse.png")
myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()
