# Create a list fruits = ["apple", "banana", "cherry"].

# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))

# Create a list of numbers from 1 to 10.

# Print the first three numbers using slicing.
# Print the last three numbers using slicing.
list = [i for i in range(1, 11)]
print(list)
print(list[0:3])
print(list[-3:])

# Start with numbers = [5, 2, 9, 1, 7] and do the following:

# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.
numbers = [5, 2, 9, 1, 7]
numbers.sort()
numbers.append(10)
numbers.remove(2)
print(numbers)

# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")

# Create a tuple coordinates = (10, 20) and print both elements.
coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)
print(coordinates[0])
print(coordinates[1])


# coordinates[0] = 50
# print(coordinates)

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
coord = list(coordinates)
coord[0] = 50
coordinates = tuple(coord)
print(coordinates)

# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
my_set = {1, 2, 3, 3, 4}
print(my_set)

# # Add 5 to the set, remove 2, and check if 4 is in the set.
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
print(4 in my_set)


# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
# Find their:
# Union
# Intersection
# Difference (a - b)

a = {1, 2, 3}
b = {3, 4, 5}


c = a.union(b)
print(c)
d = a.intersection(b)
print(d)
e = a.difference(b)
print(e)

# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
# Print the value of "name".
# Change "grade" to "A+".
# Add a new key "city" with value "Delhi".

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
print(student)
student["city"] = "Delhi"
print(student)


# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

friends = {"Alice": "12345", "Bob": "67890", "Charlie": "54321"}
print(friends.keys())
print(friends.values())
for name, number in friends.items():
    print(f"{name}: {number}")

# Write a program that takes a list of numbers and removes all duplicates using a set.
numbers = [1, 2, 3, 3, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)


# Given a dictionary of products and their prices, find the product with the highest price.
dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 12}
max_price_product = max(dict, key=dict.get)
print(
    f"The product with the highest price is {max_price_product} with price {dict[max_price_product]}")


# Write a program that merges two dictionaries into one.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
