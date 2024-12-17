def solution(n):
    answer = 0
    nanum = n // 7
    namuji = n % 7
    
    if namuji == 0:
        return nanum
    else:
        nanum += 1
        return nanum