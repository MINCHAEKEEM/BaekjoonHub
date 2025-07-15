def solution(my_string, is_prefix):
    answer = 0
    box = ""
    
    for string in my_string:
        if box != is_prefix:
            box += string
        pass
    
    if box == is_prefix:
        answer += 1
    return answer