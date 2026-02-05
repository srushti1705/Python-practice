def convert_str_to_int(str_num_list):
    int_list = [] 
    for i in str_num_list:
        num = int(i) 
        int_list.append(num) 
    return int_list 
    
def convert_to_key_value_pairs(keys_list, values_list):
    new_dict = {} 
    number_of_keys = len(keys_list) 
    for i in range(number_of_keys):
        key = keys_list[i] 
        value = values_list[i] 
        new_dict[key] = value 
    return new_dict

keys_of_first_dict = input().split() 
values_of_first_dict = input().split() 
keys_of_second_dict = input().split() 
values_of_second_dict = input().split() 

values_of_first_dict = convert_str_to_int(values_of_first_dict)
values_of_second_dict = convert_str_to_int(values_of_second_dict)

student_details_1 = convert_to_key_value_pairs(keys_of_first_dict, values_of_first_dict) 
student_details_2 = convert_to_key_value_pairs(keys_of_second_dict, values_of_second_dict) 

student_details_1.update(student_details_2) 
student_details = student_details_1.items() 
student_details = sorted(student_details) 
print(student_details)