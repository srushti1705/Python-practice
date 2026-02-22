x = "Global variable" 
def foo():
    global x 
    x = "Modified global variable"
    y = "Local variable"
    print(y)
    print(x) 
print(x)
foo() 
print(x)
