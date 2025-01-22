from collections import Counter
def solution(s):
    answer = ''
    count_s = Counter(s)
    
    for k, v in count_s.items():
        if v == 1:
            answer += k
    print(count_s)
    return ''.join(sorted(answer))

# s에서 단 한번만 등장한 문자(들)를 사전상의 순서대로 정렬한 문자열 반환하기
# 문자가 없을 경우 빈문자열
# 카운터 사용해서 문자 빈도 파악하기
# 이프문 조건에 문자출현 빈도수 달기