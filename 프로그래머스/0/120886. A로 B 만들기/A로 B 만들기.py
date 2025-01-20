from collections import Counter
def solution(before, after):
    answer = 0
    count_before = Counter(before)
    count_after = Counter(after)
    
    if count_before.items() == count_after.items():
        answer+=1
    else:
        return answer

    print(count_before.items(), count_after.items())
    return answer

# 숨어있는 숫자의 덧셈(2) 문제풀이 방식 응용해볼 것