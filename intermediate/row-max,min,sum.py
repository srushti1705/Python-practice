def print_max_min_sum_for_row_wise(num_list):
    max_list = [] 
    min_list = [] 
    sum_list = [] 
    for i in num_list:
        maximum_number = max(i) 
        max_list.append(maximum_number) 
        minimum_number = min(i) 
        min_list.append(minimum_number) 
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

max_min_sum_list = print_max_min_sum_for_row_wise(num_list)
for i in max_min_sum_list:
    print(i)
