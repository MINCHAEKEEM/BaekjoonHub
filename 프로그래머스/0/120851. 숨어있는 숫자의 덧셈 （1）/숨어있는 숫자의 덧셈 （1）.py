def solution(my_string):
    nature = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = 0
    for mystr in range(len(my_string)):
        for mystr in my_string:
            if mystr in nature:
                answer += int(mystr)
        return answer

# 문자 안에 내포된 각 숫자들의 합 구하기
# 문자 안에 숫자도 문자인데 어떻게 구별해낼 것인지?