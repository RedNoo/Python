from tkinter import *


def submit():
    print("temperature is " + str(scale.get()) + " degrees C")


window = Tk()

image = PhotoImage(file="warehouse.png")
label = Label(image=image)
label.pack()

scale = Scale(window,
              from_=1000,
              to=150,
              length=600,
              orient=VERTICAL,
              font=("Verdana",20),
              tickinterval=10,
              #showvalue=0,
              troughcolor='#69eaff',
              fg="#ff1c00"


              )
scale.set(((scale["from"] - scale["to"])/2) +scale["to"])
scale.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()


window.mainloop()
