# num = input("Enter a number: ")
# print("You entered:", num)

# if int(num) > 0:
#     print("The number is positive.")
# elif int(num) == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")


# age = int(input("Enter your age: "))
# if (age > 18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# num = int(input("Enter a number :"))

# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


# day_num = int(input("Enter day number (1-7): "))
# match day_num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number.")


# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# operation = input("Enter operation (+, -, *, /): ")
# match operation:
#     case "+":
#         print("Sum:", num1 + num2)
#     case "-":
#         print("Difference:", num1 - num2)
#     case "*":
#         print("Product:", num1 * num2)
#     case "/":
#         if num2 != 0:
#             print("Quotient:", num1 / num2)
#         else:
#             print("Error: Division by zero.")
#     case _:
#         print("Invalid operation.")

# n = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#     print(n, " X ", i, " = ", n*i)


# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)


# for i in range(1, 5):
#     print("*"*i)

# sum = 0
# i = 1
# while i <= 100:
#     print(i)
#     sum += i
#     i += 1
# print("The sum is:", sum)


# password = "Y2k123"
# entered_pass = input("Enter the password: ")

# while (entered_pass != password):
#     print("Incorrect password. Try again.")
#     entered_pass = input("Enter the password: ")


# num = 45222

# print(str(num))
# print(int(str(num)[::-1]))


# for i in range(1, 11):
#     print(i)
#     if (i == 7):
#         break


# for i in range(1, 11):

#     if (i == 7):
#         continue
#     print(i)

for i in range(1, 6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)
