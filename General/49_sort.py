import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

studentList = ["Veli", "Rıza", "Ilgaz", "Aycan", "Ömer"]

studentList.sort(key=locale.strxfrm, reverse=True)

print(studentList)

studentTuple = ("Veli", "Rıza", "Ilgaz", "Aycan", "Ömer")

studentListFromTuple = sorted(studentTuple, key=locale.strxfrm, reverse=True)

print(studentListFromTuple)

newStudents = [
    ("Veli", "F", 10),
    ("Ömer", "A", 98),
    ("Rıza", "C", 78),
]

name = lambda names:names[0]
newStudents.sort(key=name)

print(newStudents)
