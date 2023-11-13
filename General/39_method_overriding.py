class Animal:

    def eat(self):
        print("this animal eating")

class Rabbit(Animal):
    def eat(self):
        print("this rabbit is eat carrot")


rabbit = Rabbit()

rabbit.eat()
