from tkinter import *

def display():
    if(x.get() == 1):
        print("you agree!")
    else:
        print("you don't agree!")

window = Tk()

photo = PhotoImage(file="warehouse.png")

x = IntVar()
check_button =Checkbutton(window,
                          text="I agree",
                          variable=x, onvalue=1,
                          offvalue=0,
                          command=display,
                          font=('Arial',20),
                          fg="#00ff00",
                          bg="black",
                          activebackground="#00ff00",
                          activeforeground="black",
                          pady=5,
                          padx=5,
                          image=photo,
                          compound="top"
                          )
check_button.pack()

window.mainloop()
