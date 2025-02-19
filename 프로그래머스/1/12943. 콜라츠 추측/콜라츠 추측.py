def solution(num):
    count = 0  # 반복 횟수를 저장하는 변수
    
    while num != 1:  # num이 1이 될 때까지 반복
        if count >= 500:  # 500번 이상 반복하면 -1 반환
            return -1
        
        if num % 2 == 0:  # 짝수라면
            num //= 2  # 2로 나눔
        else:  # 홀수라면
            num = num * 3 + 1  # 3을 곱하고 1을 더함

        count += 1  # 횟수 증가
    
    return count  # 1이 되었을 때의 반복 횟수 반환