def solution(n):
    # 콜라츠 수열을 저장할 리스트를 초기값 n으로 시작합니다.
    collatz_seq = [n]
    
    # n이 1이 될 때까지 반복합니다.
    while n != 1:
        # n이 짝수이면 2로 나눕니다.
        if n % 2 == 0:
            n //= 2
        # n이 홀수이면 3*n + 1을 계산합니다.
        else:
            n = 3 * n + 1
        
        # 새로 계산된 n을 수열에 추가합니다.
        collatz_seq.append(n)
    
    return collatz_seq