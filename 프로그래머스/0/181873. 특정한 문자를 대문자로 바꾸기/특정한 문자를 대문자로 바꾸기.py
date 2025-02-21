def solution(my_string, alp):
    answer = ''
    
    for mystr in my_string:
        if mystr == alp:
            new_mystr = mystr.upper()
            answer += new_mystr
        else:
            answer += mystr
    return answer