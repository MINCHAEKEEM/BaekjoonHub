def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    # 공통 분모 계산
    common_denom = lcm(denom1, denom2)
    print(f"공통 분모: {common_denom}")  # 4
    
    # 분자 계산
    new_numer1 = numer1 * (common_denom // denom1)
    new_numer2 = numer2 * (common_denom // denom2)
    print(f"조정된 분자1: {new_numer1}")  # 2
    print(f"조정된 분자2: {new_numer2}")  # 3
    
    total_numer = new_numer1 + new_numer2
    print(f"분자 합: {total_numer}")  # 5
    
    # 기약 분수로 만들기
    divisor = gcd(total_numer, common_denom)
    print(f"최대공약수: {divisor}")  # 1
    
    result = [total_numer // divisor, common_denom // divisor]
    print(f"결과: {result}")  # [5, 4]
    return result


