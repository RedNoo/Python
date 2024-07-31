from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("oop 2")
        self.geometry("400x400")

        self.my_label = Label(self, text="Enter Your Name", font=("Ubuntu",24))
        self.my_label.pack(pady=20)

        self.my_entry = Entry(self, width=20, font=("ubuntu",24))
        self.my_entry.pack(pady=20)

        self.my_button = Button(self, text="Pop up", command=self.popup )
        self.my_button.pack(pady=20)
    
    def popup(self):
        if self.my_entry.get():
            messagebox.showinfo("hello", f"Hello {self.my_entry.get()}")
        else:
            messagebox.showerror("hello", "you forgot to type in your name !")






app = App()

app.mainloop()