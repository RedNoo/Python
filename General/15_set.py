# set - unordered, un indexed, no duplicate

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup", "knife"}
utensils.add("fork")

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)

#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))

print(utensils)

dinner_table = utensils.union(dishes)


for x in dinner_table:
    print(x)
