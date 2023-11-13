class Animal:
    alive = True

    def eat(self):
        print("this animal eating")

    def sleep(self):
        print("this animal sleeping")

class Rabbit(Animal):
    def run(self):
        print("this rabbit run")

class Fish(Animal):
    def swim(self):
        print("this fish swim")

class Hawk(Animal):
    def fly(self):
        print("this hawk fly")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
fish.swim()
