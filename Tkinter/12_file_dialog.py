from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(initialdir="/home/kayayan/Desktop/",
                                          title="Open File",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*"))
                                          )
    file = open(filepath, "r")
    content = file.read()
    text.delete("1.0", END)
    text.insert("1.0", content)
    file.close()


def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=(("text files", "*.txt"), ("all files", "*.*")),
                                    title="Save file"
                                    )
    if file is None:
        return
    file_text = str(text.get("1.0", END))
    file.write(file_text)
    file.close()


window = Tk()

text = Text(window)
text.pack()

button = Button(window, text="open", command=open_file)
button.pack()
button = Button(window, text="save", command=save_file)
button.pack()

window.mainloop()
