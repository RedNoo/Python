from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

def order():
    if x.get() == 0:
        print(food[0])
    elif x.get() == 1:
        print(food[1])
    elif x.get() == 2:
        print(food[2])
    else:
        print("huh?")


window = Tk()

photo = PhotoImage(file="warehouse.png")
foodImages = [photo, photo, photo]

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=10,
                              pady=5,
                              font=("Zekton", 50),
                              image= foodImages[index],
                              compound="left",
                              indicatoron=0,
                              width=400,
                              command=order
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
