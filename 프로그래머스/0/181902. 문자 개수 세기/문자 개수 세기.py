import re

def solution(my_string):
    answer = [0] * 52  # 알파벳 개수를 담을 리스트 (대문자 26개 + 소문자 26개)
    
    # 알파벳 리스트 (A-Z, a-z 순서)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # 문자열에서 알파벳만 찾아 리스트로 저장
    letters = re.findall(r'[a-zA-Z]', my_string)

    # 찾은 알파벳들의 개수 카운트
    for char in letters:
        index = alphabet.index(char)  # 해당 알파벳의 인덱스 찾기
        answer[index] += 1  # 해당 알파벳 개수 증가

    return answer

import re

def solution(my_string):
    answer = [0] * 52 
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    mystring = re.findall(r'[a-zA-Z]', my_string)

    for mystr in mystring:
        index = alphabet.index(mystr)  # 해당 알파벳의 인덱스 찾기
        answer[index] += 1  # 해당 알파벳 개수 증가

    return answer