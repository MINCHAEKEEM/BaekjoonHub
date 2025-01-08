def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer

# numlist 리스트 안에서 n의 배수가 아닌 숫자들을 제거한 새 리스트를 반환하기