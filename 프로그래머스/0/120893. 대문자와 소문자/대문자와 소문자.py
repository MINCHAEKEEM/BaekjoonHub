def solution(my_string):
    answer = ''
    for mystr in my_string:
        if mystr.islower() is True:
            answer += mystr.upper()
        else:
            answer += mystr.lower()
    return answer

# my_string 이 대문자면 소문자로, 소문자면 대문자로 변환