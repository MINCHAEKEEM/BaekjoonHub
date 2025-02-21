def solution(num_list):
    new_num_list = enumerate(num_list, 1)
    hol = 0
    jjak = 0
    
    for idx, num in new_num_list:
        if idx % 2 != 0:
            hol += num
        else:
            jjak += num
            
    return max(hol, jjak)