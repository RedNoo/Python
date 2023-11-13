class Car:
    def turn_on(self):
        print("you start the engine")
        return  self

    def drive(self):
        print("you drive the car")
        return self


car = Car()

car.turn_on()\
    .drive()


