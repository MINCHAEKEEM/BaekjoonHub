# from collections import Counter # 일단 카운터 임포트
# def solution(my_string):
#     countstr = Counter(my_string)
    
#     return ''.join([k for k, v in countstr.items()])  
def solution(my_string):
    s = set()  # 이미 본 문자를 저장할 집합
    # result = [] # 결과를 담을 리스트
    
    return ''.join([mystr for mystr in my_string if not (mystr in s or s.add(mystr))])
        # if mystr not in s:  # 중복되지 않은 문자라면
        #     s.add(mystr)    # 집합에 추가
        #     result.append(mystr)  # 결과 리스트에 추가
    
    # return ''.join(result)  # 리스트를 문자열로 변환
    
    