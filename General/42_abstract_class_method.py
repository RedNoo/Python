from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive to car")

class Motorcycle(Vehicle):
    def go(self):
        print("you drive to motorcycle")


car = Car()
motorcycle  = Motorcycle()

car.go()
motorcycle.go()
