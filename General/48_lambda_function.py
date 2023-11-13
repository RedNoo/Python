def double(x):
    return x * 2


print(double(5))

double2 = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double2(5))
print(multiply(5, 6))
print(add(1, 2, 3))
print(full_name("jane", "doe"))
print(age_check(18))
