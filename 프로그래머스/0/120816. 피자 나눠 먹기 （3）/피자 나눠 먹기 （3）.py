def solution(slice, n):
    answer = 0
    eat = n // slice
    hungry = n % slice
    
    if hungry == 0:
        return eat
    else:
        eat += 1
        return eat