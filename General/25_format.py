number = 1000

animal = "cow"
item = "moon"

print("the {} jumped over the {}".format(animal, item))
print("the {0} jumped over the {1}".format(animal, item))
print("the {a} jumped over the {b}".format(b=item, a=animal))

text = "the {} jumped over the {}"
print(text.format(animal, item))

name = "jane"

print("Hello my name is {}.Nice to meet you.".format(name))
print("Hello my name is {:10}.Nice to meet you.".format(name))
print("Hello my name is {:<10}.Nice to meet you.".format(name))
print("Hello my name is {:>10}.Nice to meet you.".format(name))
print("Hello my name is {:^10}.Nice to meet you.".format(name))

number = 3.14159
print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))

number = 1000

print("The number  is {:.3f}".format(number))
print("The number  is {:,}".format(number))
print("The number  is {:b}".format(number))
print("The number  is {:o}".format(number))
print("The number  is {:X}".format(number))
print("The number  is {:E}".format(number))




