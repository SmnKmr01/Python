# WAP to find the factorial of a number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    factorial = 1
else:
    for i in range(1, num + 1):
        factorial *= i
print(f"The factorial of {num} is: {factorial}")
