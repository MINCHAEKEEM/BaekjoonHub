def solution(s):
    answer = True
    box = []
    
    for i in s:
        if i == '(':
            box.append(i)  
        else:
            if box: 
                box.pop()
            else:
                return False

    return len(box) == 0