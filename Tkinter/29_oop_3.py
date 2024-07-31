from tkinter import *
from tkinter import filedialog

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("oop 3")
        self.geometry("700x700")


        self.my_text = Text(self, width=80, height=20)
        self.my_text.pack(pady=20)

        self.my_button = Button(self, text="open file", command=self.file)
        self.my_button.pack(pady=20)



    def file(self):
        self.my_file = filedialog.askopenfilename(initialdir="", title="select e a file", filetypes=(("python files","*.py"),("All files","*.*")))

        if self.my_file:
            get_contents = open(self.my_file,"r")
            self.my_text.insert(END, get_contents.read())


app = App()
app.mainloop()