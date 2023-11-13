from car import Car

car_1 = Car("Checvy","Corvette",2021, "blue")
car_2 =Car("Ford","Masteng",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

car_1.wheels = 6
print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)