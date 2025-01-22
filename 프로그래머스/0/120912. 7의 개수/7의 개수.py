def solution(array):
    answer = 0
    seven = ''
    
    for i in str(array):
        if '7' in i:
            seven += i
        else:
            if seven:
                answer += seven.count('7')
                seven = ''
    if seven:
        answer += seven.count('7')
        
    print(seven)
    return answer

# array 안에 7이 총 몇개 있는지 개수 반환하기