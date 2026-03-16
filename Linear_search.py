# Linear Search Function
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# Main Program

# List of numbers
arr = [5, 12, 7, 20, 9, 15]

# Element to search
target = 20

# Call search function
result = linear_search(arr, target)

# Print result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
