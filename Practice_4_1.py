from my_utils import is_even
import requests
import math
A = math.sqrt(144)
B = math.radians(90)
print(A, B)


a = requests.get("https://www.google.com")
print(a.json())


def increment():
    counter = 0
    counter += 1
    print(counter)


increment()


def multiply(a, b):
    '''This function will multiply two numbers a and b'''
    return a * b


print(multiply(4, 5))
print(multiply.__doc__)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


print(safe_divide(10, 2))  # Output: 5.0


# Example usage
print(is_even(4))   # True
print(is_even(7))   # False
