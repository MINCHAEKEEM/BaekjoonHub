def solution(my_string, num1, num2):
    my_list = list(my_string) # 문자열을 리스트로 변환
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1] # 문자 교체
    return "".join(my_list) # 리스트를 문자열로 변환

# my_string 에서 my_string[num1]번째 my_string[num2]번째 글자를 서로 바꿀 것