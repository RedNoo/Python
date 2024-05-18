#Lists : ordered, mutable, allowa dublicate elements
food = ["pizza", "hamburger", "hotgod", "spaghetti"]
food[0] = "sushi"
print(food[0])

food.append("ice cream")
food.remove("sushi")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:
    print(x)