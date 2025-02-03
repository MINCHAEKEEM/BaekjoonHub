def solution(s):
    a = 0
    b = 0

    p_list = ['p', 'P']
    y_list = ['y', 'Y']
    
    for elem in s:
        if elem in p_list:
            a += 1
        elif elem in y_list:
            b += 1
    if a == b:
        return True
    elif a != b:
        return False
    elif a == 0 and b == 0:
        return True