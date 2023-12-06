from tkinter import *


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print(food)


# print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    # listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Hamburger")
listbox.insert(2, "Soup")
listbox.insert(2, "Salad")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()
