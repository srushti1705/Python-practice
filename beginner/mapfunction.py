def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5] 
result = map(square, numbers) 
numbers_squared = list(result) 
print(numbers_squared) 

line = input("Enter numbers separated by space: ") 
str_nums = line.split()
map_obj = map(int, str_nums)
numbers = list(map_obj)
print(numbers) 