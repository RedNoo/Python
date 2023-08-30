import tkinter as tk

form = tk.Tk()
form.title("this is the window title")
label1 = tk.Label(form, text="Hello label 1")
label1.pack()
label2 = tk.Label(form, text="Hello Label 2", fg='red')
label2.pack()
label3 = tk.Label(form, text="Hello Label 3", bg='green')
label3.pack()
label4 = tk.Label(form, text="Hello label 4", font='Times 15 italic')
label4.pack()
form.geometry('500x200+400+300')
# form.minsize(500,400)
# form.maxsize(600,600)

# full-screen
# form.attributes('-zoomed', True)

# form.resizable(False, False)

# minimized
# form.state('iconic')

# transparent
form.wait_visibility(form)
form.wm_attributes('-alpha', 0.3)

form.mainloop()
