lower = int(input("Enter a lower limit of interval : "))
upper = int(input("Enter an upper limit of interval : "))

for num in range(lower,upper + 1):
    order = len(str(num))
    sum = 0 
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")