#Program to swap two variables

a = input("Enter first variable: ")
b = input("Enter second variable: ")

print(f"Before swapping: a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")


#OR # Using a function to swap variables

def swap_variables(x, y):
    x, y = y, x
    return x, y
a, b = swap_variables(a, b)
print(f"After swapping: a = {a}, b = {b}")