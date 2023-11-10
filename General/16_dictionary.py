# dictionary changeable, unordered, unique pairs, fast

capitals = {'USA': 'Washington DC',
            'India': "New Delhi",
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':"Washington"})
capitals.pop('China')


print(capitals["Russia"])
print(capitals.get('Russia_'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.clear()
for key, value in capitals.items():
    print(key,value)