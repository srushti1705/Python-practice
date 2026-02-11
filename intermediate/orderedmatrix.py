def convert_str_to_int(inputs):
    int_list = [] 
    for i in inputs:
        num = int(i) 
        int_list.append(num) 
    return int_list

m, n = input().split()
m = int(m)
n = int(n) 
matrix = []
for i in range(m):
    inputs = input().split() 
    int_list = convert_str_to_int(inputs)
    matrix.extend(int_list)
    matrix.sort()
index = 0
for i in range(m):
    for j in range(n):
        print(matrix[index], end=" ") 
        index += 1 
    print() 
    
# Sample Input 
# 3 3
# 1 20 3
# 30 10 2
# 5 11 15