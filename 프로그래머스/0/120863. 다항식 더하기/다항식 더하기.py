def solution(polynomial):
    # 일차항 계수와 상수항을 저장할 변수 초기화
    coefficient = 0  # x의 계수
    constant = 0     # 상수항
    
    # 공백을 기준으로 항을 분리
    terms = polynomial.split(" + ")
    
    for term in terms:
        if 'x' in term:  # 항에 x가 포함된 경우
            if term == 'x':  # 계수가 생략된 경우 (계수 1)
                coefficient += 1
            else:  # 계수가 명시된 경우
                coefficient += int(term.replace('x', ''))
        else:  # 상수항인 경우
            constant += int(term)
    
    # 결과를 문자열로 조합
    result = []
    if coefficient:  # x 항이 존재하면 추가
        result.append(f"{coefficient}x" if coefficient > 1 else "x")
    if constant:  # 상수항이 존재하면 추가
        result.append(f"{constant}")
    
    return " + ".join(result)  # 결과를 공백과 '+'로 연결

# 테스트 코드
print(solution("3x + 7 + x"))  # "4x + 7"
print(solution("x + x + x"))   # "3x"