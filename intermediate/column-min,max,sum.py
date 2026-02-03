def get_transpose_of_matrix(matrix, m, n):
    transpose_matrix = [] 
    for i in range(n):
        row = [] 
        for j in range(m):
            row.append(matrix[j][i]) 
        transpose_matrix.append(row) 
    return transpose_matrix


def print_max_min_sum_for_row_wise(num_list):
    max_list = [] 
    min_list = [] 
    sum_list = [] 
    for i in num_list:
       maximum = max(i) 
       max_list.append(maximum) 
       minimum = min(i) 
       min_list.append(minimum) 
       total = sum(i) 
       sum_list.append(total) 
    return max_list, min_list, sum_list


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

transpose_matrix = get_transpose_of_matrix(num_list, m, n)
result = print_max_min_sum_for_row_wise(transpose_matrix)
for i in result:
    print(i)