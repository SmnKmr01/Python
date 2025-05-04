a = input("Enter the number:")
print(f"MUltiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f"{a} * {i} = {int(a)*i}")
except :
    print("Sorry some error occurred")
 

print("Some line of code")
print("End of code")


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")


try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index out of range.")