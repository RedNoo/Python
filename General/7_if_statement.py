age = int(input("How old are you? : "))

if age >= 18:
    print("you are an adult")
elif age < 0:
    print("you haven't born yet")
else:
    print("you are a child")

temp = int(input("what is the remporature outside ? : "))

logic = temp >= 0 and temp <= 30

if logic:
    print("temperature is good today")
    print("go outside")
elif not(logic):
    print("temperature is bad today")
    print("stay inside")
