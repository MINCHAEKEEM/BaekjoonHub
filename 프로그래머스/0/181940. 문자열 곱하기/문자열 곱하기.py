def solution(my_string, k):
    answer = ''
    
    if len(my_string) != 0:
        my_string *= k
        answer += my_string
    return answer