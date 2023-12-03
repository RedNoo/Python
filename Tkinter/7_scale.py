from tkinter import *


def submit():
    print("temperature is " + str(scale.get()) + " degrees C")


window = Tk()

scale = Scale(window,
              from_=0,
              to=200,
              length=600,
              orient=VERTICAL,


              )
scale.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()


window.mainloop()
