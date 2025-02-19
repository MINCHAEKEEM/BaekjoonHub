def solution(my_string, queries):
    # 문자열을 리스트로 변환 (mutable하게 변경)
    str_list = list(my_string)
    
    # 각 쿼리를 순회하며 문자열 일부를 뒤집음
    for s, e in queries:
        str_list[s:e+1] = str_list[s:e+1][::-1]  # 슬라이싱을 이용한 역순 처리

    # 리스트를 문자열로 변환하여 반환
    return "".join(str_list)