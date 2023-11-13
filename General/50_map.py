store = [
    ("shirt", 20.00),
    ("pants", 10.00),
    ("jacket", 30.00),
]

to_euros = lambda data: (data[0], data[1] * 0.82)

store_euros = list(map(to_euros, store))

print(store_euros)
