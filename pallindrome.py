
# Pallindrome(Using String Slicing)
number = int(input("Enter a number: "))

def is_palindrome(number):
    str_num = str(number)
    reversed_num = str_num[::-1]
    return str_num == reversed_num
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


#pallindrome(Using reverse function)
def is_palindrome(number):
    str_num = str(number)
    reversed_num = ''.join(reversed(str_num))
    return str_num == reversed_num

#palindrome(using for loop)
def is_palindrome(number):
    str_num = str(number)
    reversed_num = ""
    for char in str_num:
        reversed_num = char + reversed_num
    return str_num == reversed_num