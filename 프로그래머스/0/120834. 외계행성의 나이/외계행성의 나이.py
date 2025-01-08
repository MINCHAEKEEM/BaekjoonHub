def solution(age):
    trans = {'0':'a' , '1':'b' , '2':'c' , '3':'d' , '4':'e', '5':'f', '6':'g',  '7':'h', '8':'i', '9':'j'}
    answer = ''
    
    for age2 in str(age):
        if str(age2) in trans:
            answer += trans.get(age2)
    return answer
    
    
    
# 프로그래머스-962식 나이 반환하기
# 프로그래머스-962 나이는 알파벳으로 나타냄
# a는 0부터 순차적으로 j까지 9를 나타냄