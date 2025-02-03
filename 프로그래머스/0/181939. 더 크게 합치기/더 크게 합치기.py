def solution(a, b):
    exclusive = int(str(a) + str(b))
    revexclusive = int(str(b) + str(a))
    answer = 0
    
    if exclusive > revexclusive:
        answer += exclusive
    elif exclusive == revexclusive:
        answer += exclusive
    else:
        answer += revexclusive
    return answer