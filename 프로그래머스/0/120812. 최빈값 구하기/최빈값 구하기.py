from collections import Counter

def solution(array):
    array_count = Counter(array)
    max_count = max(array_count.values())
    
    mode = [k for k, v in array_count.items() if v == max_count]
        
    if len(mode) > 1:
        return -1
    else:
        return mode[0]


