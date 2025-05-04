a = input("Enter a word : ")
if(len(a) >= 3):
    b  = a[1:]+a[-4]
    modified = input("Enter the random character for the starting: ")
    modified2 = input("Enter the random character for the ending: ")
    c= modified + b + modified2
    print(c)
else:
    print(a[::-1])
x = input("Enter the decode: ")
if(len(x) >= 3):
    y = x[3:-4]
    z = x[-4]
    b = x+y
    print(b)
else:
    print(x[::-1])