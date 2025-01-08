def solution(array):
    answer = []
    max_array = max(array)
    index_array = array.index(max_array)
    for num in array:
        if num == max_array:
            answer.append(num)
            answer.append(index_array)
    return answer

# 리스트 안에서 제일 큰 수와 그 수의 인덱스 위치를 담은 리스트 반환하기