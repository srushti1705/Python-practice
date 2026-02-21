from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split())) 

def is_even(num):
    return num % 2 == 0

def square(num):
    return num ** 2

def add(x, y):
    return x + y

even_numbers = list(filter(is_even, numbers))
squared_even_numbers = list(map(square, even_numbers))
if squared_even_numbers:
    result = reduce(add, squared_even_numbers)
else:
    result = 0
print("The sum of squares of even numbers is:", result) 