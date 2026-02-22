try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
