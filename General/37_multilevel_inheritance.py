class Organisim:
    alive = True


class Animal(Organisim):
    def eat(self):
        print("this animal eating")


class Dog(Animal):

    def bark(self):
        print("this dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

