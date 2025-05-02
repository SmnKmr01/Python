# s1 = {1,2,3,6}
# s2 = {3,6,7}

# print(s1.union(s2)) 
# print(s1,s2)
# print(s1.intersection(s2))
# s1.update(s2)
# print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities.intersection_update(cities2)
# print(cities)


#Symmetric difference
# A^B = (A-B) U (B-A) / (AUB) - (A∩B)

# cities3 = cities.difference(cities2)



# print(cities.issubset(cities2)) #False
# print(cities.isdisjoint(cities2))
# print(cities.issuperset(cities2)) #True
cities3  = {"Tokyo", "Seoul", "Kabul"}
# print(cities2.issuperset(cities3))
# print(cities3)

cities.discard("Tokyo")
print(cities)

item = cities.pop()
print(item)

cities.clear()
print(cities)