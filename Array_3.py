# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_num = int(input("Enter a max number: "))
odd_numbers = []

for i in range(1, max_num+1):
    if i % 2 != 0:
        odd_numbers.append(i)

print("List of odd numbers between 1 and", max_num, "is:", odd_numbers)
