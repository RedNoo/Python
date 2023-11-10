name = "jane doe!"

if name[0].islower():
    name = name.capitalize()

first_name = name[:4].upper()
last_name = name[5:].upper()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
