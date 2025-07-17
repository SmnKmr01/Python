# Write a prog to Print all Prime Numbers in an interval of 1-10

start = 1
end = 10
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
