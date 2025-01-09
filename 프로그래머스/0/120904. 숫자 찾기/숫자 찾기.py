def solution(num, k):
    answer = 1

    for n in str(num):
        if str(k) in str(num):
            if str(k) != n:
                answer += 1
            elif str(k) == n:
                return answer
        else:
            return -1
                

# num 안에 k가 있으면 k의 위치 수를 반환, 없으면 -1