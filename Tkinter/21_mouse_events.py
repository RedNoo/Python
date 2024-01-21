from tkinter import *

def do_something(event):
    print("worked " + str(event.x) + "," + str(event.y) )

window = Tk()

window.bind("<Button-1>", do_something) #left
window.bind("<Button-2>", do_something) #scroll
window.bind("<Button-3>", do_something) #rigt
window.bind("<ButtonRelease>", do_something)
window.bind("<Enter>", do_something)
window.bind("<Leave>", do_something)
window.bind("<Motion>", do_something)
window.mainloop()