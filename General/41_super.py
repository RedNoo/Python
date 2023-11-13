class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length


class Square(Rectangle):
    def __init__(self, width, length):
        super().__init__(width, length)

    def area(self):
        return self.width*self.length
class Cube(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height

    def volume(self):
        return self.width*self.length*self.height


square = Square(10, 10)


print(square.area())

cube = Cube(10,10,100)

print(cube.volume())