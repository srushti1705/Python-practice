def compute_consecutive_sum(int_list):
    consecutive_sum_list = []
    end_index = len(int_list) - 1
    for index in range(end_index): 
        consecutive_sum = int_list[index] + int_list[index+1] 
        consecutive_sum_list.append(consecutive_sum) 
    return consecutive_sum_list
        
def print_consecutive_sum_tri(int_list):
    while len(int_list) > 1:
        consecutive_sum_list = compute_consecutive_sum(int_list)
        print(consecutive_sum_list) 
        int_list = consecutive_sum_list
    
def convert_str_to_int(str_num_list):
    int_list = [] 
    for item in str_num_list:
        num = int(item) 
        int_list.append(num) 
    return int_list

str_num_list = input().split(",")
int_list = convert_str_to_int(str_num_list)
print(int_list)
print_consecutive_sum_tri(int_list)