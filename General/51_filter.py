friends = [
    ("Rachel", 18),
    ("Monica", 16),
    ("Joey", 19),
    ("Ross", 21)
]

age = lambda data:data[1] >= 18

drinking_bodies = list(filter(age, friends))

print(drinking_bodies)
