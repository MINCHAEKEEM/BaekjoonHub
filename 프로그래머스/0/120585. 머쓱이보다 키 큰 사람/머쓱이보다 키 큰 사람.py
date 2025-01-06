def solution(array, height):
    answer = []
    for ah in range(len(array)):
        for ah in array:
            if ah > height:
                answer.append(ah)
        return len(answer)
    

# 머쓱이 친구들 키: array(리스트)
# 머쓱이 키: height
# array와 height을 비교해서
# ***머쓱이보다 큰 사람의 수*** 를 return