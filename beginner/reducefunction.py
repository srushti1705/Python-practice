from functools import reduce

def sum_of_numbers(x, y):
    return x + y

numbers = [1, 2, 3, 4]
result = reduce(sum_of_numbers, numbers)
print(result)