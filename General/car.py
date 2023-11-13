class Car:
    wheels = 4
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("this " + self.model + " car is driving")

    def stop(self):
        print("this " + self.model + "  car is stopping")
