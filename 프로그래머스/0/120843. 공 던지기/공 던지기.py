def solution(numbers, k):
    # 공이 던져지는 순서를 순환하기 위해 인덱스를 계산합니다.
    # 한 번 던질 때마다 오른쪽으로 두 칸 이동하므로 k-1번 반복
    # 이동 후 인덱스를 numbers의 길이로 나눠 순환 구조를 만듭니다.
    return numbers[(k - 1) * 2 % len(numbers)]