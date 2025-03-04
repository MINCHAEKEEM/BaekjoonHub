def solution(myString, pat):
    answer = 0
    
    if pat.lower() in myString.lower():
        answer += 1
    else:
        return answer
    
    return answer