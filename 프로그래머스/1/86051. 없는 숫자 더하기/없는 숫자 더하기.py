def solution(numbers):
    answer = []
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    trans = {'0':0 , '1':1 , '2':2 , '3':3 , '4':4, '5':5, '6':6,  '7':7, '8':8, '9':9}
    
    for num in num_list:
        if not num in str(numbers):
            answer.append(trans.get(num))
    return sum(answer)

# numbers 길이는 9인데 안에 없는 숫자가 있음
# numbers 안에 없는 숫자들끼리 총 더한 값을 반환