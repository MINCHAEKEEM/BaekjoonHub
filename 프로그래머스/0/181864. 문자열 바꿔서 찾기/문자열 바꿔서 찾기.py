def solution(myString, pat):
    answer = 0
    box = ''
    
    for mystr in myString:
        if mystr == 'A':
            box += mystr.replace('A', 'B')
        else:
            box += mystr.replace('B', 'A')
    if pat in box:
        answer += 1
    else:
        answer
    return answer