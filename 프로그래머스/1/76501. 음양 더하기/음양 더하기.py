# 1
def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i]:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    
    return sum(answer)

# 2
def solution(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))
