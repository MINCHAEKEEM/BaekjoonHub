def solution(n):
    answer = 0
    for nn in str(n):
        answer += int(nn)
    return answer
    
# 정수 n이 주어질 때(1자리 수가 아닌듯)
# 정수 n의 ***덧셈버전 팩토리얼 만들기***