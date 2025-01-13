def solution(strArr):
    answer = []
    for strarr in strArr:
        strlist = []
        if not 'ad'in strarr:
            strlist.append(strarr)
            answer.append(''.join(strlist))
    return answer

# strArr의 요소 문자열 중, ad 글자를 포함하고 있는 모든 문자열은 제거시킨 새 리스트를 반환
# 문자열의 순서는 유지돼야함
# 포문
# 이프문 조건: ad가 strArr 안에 없을 경우