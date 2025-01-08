def solution(n):
    answer = []
    for nn in range(0,n,1):
        nn += 1
        if n % nn == 0:
            answer.append(nn)
    return answer

# 정수 n의 약수들을 오름차순으로 담은 리스트를 return