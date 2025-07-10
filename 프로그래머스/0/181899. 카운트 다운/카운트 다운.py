def solution(start_num, end_num):
    answer = []
    
    for i in range(end_num, start_num+2):
        while i != end_num:
            i -= 1
            answer.append(i)
            break
    
    return answer[::-1]


# start_num -=1  => end_num