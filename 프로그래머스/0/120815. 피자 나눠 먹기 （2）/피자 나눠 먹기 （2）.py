def gcd(a, b):
    while b:
        a, b= b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(n):
    nanum = n // 6
    namuji = n % 6
    
    if namuji != 0:
        return lcm(n, 6) // 6
    else:
        return nanum
   