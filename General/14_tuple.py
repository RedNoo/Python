# tuple - ordered and unchangeable

student = ("jane", 45, "female")

print(student.count("jane"))
print(student.index("jane"))


for x in student:
    print(x)

if "jane" in student:
    print ("jane is here")
