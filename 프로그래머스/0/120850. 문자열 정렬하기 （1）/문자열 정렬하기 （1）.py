def solution(my_string):
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = []
    
    for mystr in my_string:
        if mystr in numbers:
            answer.append(int(mystr))
            answer.sort()
    return answer

# my_string 문장 안에 있는 숫자들만 골라서 오름차순 정렬한 리스트 반환하기