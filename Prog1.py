# Write aPython prog to do arithmetical operations addition and division.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
sum_result = num1 + num2

if num2 == 0:
    print("Division by zero is not allowed")
else:
    div_result = num1/num2
    print(f"The division of {num1} by {num2} is: {div_result}")


print(f"The sum of {num1} and {num2} is: {sum_result}")
