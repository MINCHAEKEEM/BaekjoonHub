import math
def solution(balls, share):
    b = math.factorial(balls-share)
    s = math.factorial(share)
    blls = math.factorial(balls)
    return blls // (b * s)

# 문제 조건: balls개 중 share개만큼 고를 수 있는 모든 경우의 수 찾기
# 입력 예시: 3balls 2share = 3/ 5balls 3share = 10