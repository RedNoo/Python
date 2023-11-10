# kwargs dictionary

def hello(**kwargs):
    print("hello", end=" ")
    for key, val in kwargs.items():
        print(val, end=" ")


hello(title="Ms.", first="jane", last="doe", age="45")
print("")
hello(title="Mr.", first="john", last="doe", age="46")