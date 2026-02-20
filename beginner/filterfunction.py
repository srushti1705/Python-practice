def is_positive_number(n):
    return n > 0

numbers = [-2, -1, 0, 1, 2, 3] 
positive_numbers = filter(is_positive_number, numbers)
print(list(positive_numbers))