def solution(my_string):
    answer = []
    if my_string.isupper() is True:
            my_string.lower()
    for mystr in my_string.lower():
        answer.append(mystr)
        answer.sort()
    return ''.join(answer)

# my_string 안에 대문자를 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열 반환

