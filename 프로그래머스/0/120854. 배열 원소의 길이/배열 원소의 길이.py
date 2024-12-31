def solution(strlist):
    answer = []
    for i in strlist:
        if i != 0:
            answer.append(len(i))
    return answer