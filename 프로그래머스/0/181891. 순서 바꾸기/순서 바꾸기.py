def solution(num_list, n):
    answer = []
    new_num = num_list[0:n]
    afterN = num_list[n:]
    
    answer.extend(afterN)
    answer.extend(new_num)
    return answer