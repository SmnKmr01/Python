# WAP to Print the fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, ...

nterms = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1, end=', ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
