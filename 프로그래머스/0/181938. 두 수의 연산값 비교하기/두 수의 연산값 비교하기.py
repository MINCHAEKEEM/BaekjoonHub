def solution(a, b):
    answer = 0
    exclusive = int(str(a) + str(b))
    
    if exclusive == (2 * a * b):
        return exclusive
    elif exclusive > (2 * a * b):
        return exclusive
    else:
        return (2 * a * b)