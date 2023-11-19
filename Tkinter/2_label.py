from tkinter import *

window = Tk()

photo = PhotoImage(file="warehouse.png")

label = Label(window,
              text="Hello this is a label",
              font=("Arial", 40, "bold"),
              fg="#515151",
              bg="black",
              relief=RAISED,
              bd=5,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()
# label.place(x=100,y=100)

window.mainloop()
