import tkinter as tk


form = tk.Tk()
form.title("Title")
form.geometry("500x400")

def sum_function():
    print("sum function worked")

button1 = tk.Button(form, text= "Click Me", command=sum_function)
button1.pack()




form.mainloop()