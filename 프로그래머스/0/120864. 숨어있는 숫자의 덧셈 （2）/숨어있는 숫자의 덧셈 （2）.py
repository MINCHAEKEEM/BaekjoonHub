def solution(my_string):
    answer = 0
    num = ''

    for my_str in my_string:
        if my_str.isdigit(): # my_str이 숫자인 경우
            num += my_str # num에 my_str 저장
        else: # 숫자가 아닌 my_str을 만났을 경우
            if num: # num에 저장돼있는 숫자가 있다면
                answer += int(num) # answer에 정수로 변환하여 저장
                num = '' # 다시 if문을 반복동작 하기위한 변수 초기화
    if num: # 맨마지막 문자열에도 숫자가 있어서 num에 숫자가 저장된 경우
        answer += int(num) # answer에 정수 변환 저장
            
    return answer

# mystring 문자열 안에 내포된 자연수의 합 구하기
# 대신 숫자가 연속으로 붙어있으면 걘 하나의 숫자로 봐야함