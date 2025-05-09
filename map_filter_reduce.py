# def cube(x):
#     return x**3

# print(cube(3))
# l = [1, 2, 3, 4, 5]
# newl = []
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)

# newl = list(map(cube, l))
# newl = list(map(lambda x:x**3, l))
# print(newl)

#FILTER
# def filter_function(a):
#     return a > 4

# newnewl = list(filter(filter_function, l))
# print(newnewl)

# REDUCE
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def mysum(x, y):
    return x + y
sum = reduce(mysum, numbers)
print(sum) 