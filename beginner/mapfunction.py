def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5] 
result = map(square, numbers) 
numbers_squared = list(result) 
print(numbers_squared)