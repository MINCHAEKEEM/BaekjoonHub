def solution(my_string):
    answer = ''
    mom = ['a', 'e', 'i', 'o', 'u']
    for mystr in my_string:
        if mystr not in mom:
            answer += mystr
    return answer
            

# a, e, i, o, u 모음
# 문자열 my_string 매개변수에 다섯 모음 중 하나라도 들어가있을 경우
# ***모음이 제거된 문자열을 반환***