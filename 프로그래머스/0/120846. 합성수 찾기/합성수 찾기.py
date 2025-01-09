def solution(n):
    answer = 0
    for i in range(4,n+1):
        divisor = 0
        for j in range(1,n+1):
            if i % j == 0:
                divisor += 1
        if divisor >= 3:
            answer += 1
    return answer

# n보다 작은 범위의 숫자면서 약수가 3개 이상인 숫자 갯수 찾기