first_name = "john"
last_name = "doe"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))

age = 46
age  += 1
print(age)
print(type(age))
print("your age is "  + str(age))

height = 250.5
print("your height is " + str(height) + "cm")
print(type(height))

human = True
print("are you a human ? " + str(human))
print(type(human))

#multiple assignment
name, age, attractive = "jane", 45, True
print(name)
print(age)
print(attractive)

jane_age = john_age = 45
print(jane_age)
print(john_age)