from tkinter import *




class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter OOP")
        self.geometry('700x450')

        self.my_label = Label(self, text="Hello World")
        self.my_label.pack(pady=20)

        self.my_button = Button(self, text="Change Text", command=self.change)
        self.my_button.pack(pady=20)

        self.status = True

        self.f1 = My_frame(self)

    def change(self):
        
        if self.status == True:
            self.f1.pack_forget()
            self.my_label.config(text="Goodby World")
            self.status = False
        else:
            self.f1.pack()
            self.my_label.config(text="Hello World")
            self.status = True
        

class My_frame(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.my_button_1 = Button(self, text= "Change", command=parent.change)
        self.my_button_2 = Button(self, text= "Change", command=parent.change)
        self.my_button_3 = Button(self, text= "Change", command=parent.change)

        self.my_button_1.grid(row=0, column=0, padx=10)
        self.my_button_2.grid(row=0, column=1, padx=10)
        self.my_button_3.grid(row=0, column=2, padx=10)


app = App()
app.mainloop()