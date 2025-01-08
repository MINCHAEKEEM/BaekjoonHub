def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        answer.extend(numbers[:-1])
        return answer
    else:
        answer.extend(numbers[1:])
        answer.append(numbers[0])
        # answer[-1] -= 2
        # answer[-2] += 2
        return answer
# numbers 리스트의 원소를
# direction 방향으로 한칸씩 이동한
# 리스트 반환하기
# 다이렉션 방향은 왼쪽, 오른쪽 둘 중 하나
# 이진법 좌측시프트, 우측시프트 와 동작원리 똑같음