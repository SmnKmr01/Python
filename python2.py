import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

if(timestamp<12):
    print("Good Morning")
elif(timestamp<=17):
    print("Good Afternoon")   
else:
    print("Good night")

    