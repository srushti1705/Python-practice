def anti_diagonal_elements(num_list, m, n):
    for s in range(m+n-1):
        for i in range(m):
            for j in range(n):
                if i + j == s:
                    print(num_list[i][j], end=" ")
        print()
    
def convert_str_to_int(list_a):
    int_list = [] 
    for i in list_a:
        num = int(i) 
        int_list.append(num) 
    return int_list

m, n = input().split() 
m, n = int(m), int(n) 
num_list = [] 

for i in range(m):
    list_a = input().split() 
    list_a = convert_str_to_int(list_a)
    num_list.append(list_a) 
    
anti_diagonal_elements(num_list, m, n)

# Sample Input
# 2 3
# 1 5 5
# 2 7 8 