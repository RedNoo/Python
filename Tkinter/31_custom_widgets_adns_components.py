from tkinter import *

root = Tk();

root.title("Custom Widget")
root.geometry("700x450")


class My_widget(Frame):
    def __init__(self,parent,label_text,button_text, button_name):
        super().__init__(master=parent)

        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1),weight=1, uniform="z")

        Label(self,text=label_text, font=("ubuntu",18)).grid(row=0, column=0, sticky="nsew")
        Button(self, text=button_text, command=lambda :self.change(button_name)).grid(row=0,column=1, sticky="nsew")

        self.pack(expand=True, fill=BOTH, padx=10, pady=10)
    def change(self, name):
        if name == "my_button1":
            root.title ("1") 
        elif name == "my_button2":
            root.title ("2") 
        elif name == "my_button3":
            root.title ("3") 



My_widget(root, "Text_1", "Button_1", "my_button1")
My_widget(root, "Text_2", "Button_2", "my_button2")
My_widget(root, "Text_3", "Button_3", "my_button3")



root.mainloop()


