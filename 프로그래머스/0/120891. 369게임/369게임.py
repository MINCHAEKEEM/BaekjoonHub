def solution(order):
    answer = 0
    clap = ['3', '6', '9']
    for claptime in str(order):
        if claptime in clap:
            answer += 1
    return answer

# 박수 횟수 반환
# order 변수 안에 3, 6, 9가 있으면 박수 += 1