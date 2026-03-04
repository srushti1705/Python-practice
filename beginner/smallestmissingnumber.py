numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
numbers.sort()
num = 1
for i in numbers:
    if i == num:
        num += 1
    elif i > num:
        break
print(num)

    