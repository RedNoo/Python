import os

source = "test.txt"
destination = "/home/kayayan/Desktop/test.txt"

try:
    if os.path.exists(destination):
        print("there is already file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " File not found")
