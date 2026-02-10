def rotation(S1, S2):
    rotation_time = 0 
    if S1 == S2:
        return 0
    for i in range(len(S1)):
        first_part =  S1[:len(S1)-1] 
        second_part = S1[len(S1)-1]
        S1 = second_part + first_part
        rotation_time += 1 
        if S1 == S2:
            return rotation_time 
    return "No Match"

S1 = input()
S2 = input()
print(rotation(S1, S2))
# Sample Input
# python
# onpyth 