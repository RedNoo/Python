def loud(text):
    return text.upper()


def quiet(text):
    return text.lower();


def hello(func): #higher order function - argument function
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):  #higher order function - return a function
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))