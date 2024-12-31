from collections import Counter
def solution(s1, s2):
    lst1 = []
    lst1.extend(s1)
    lst1.extend(s2)
    
    count_lst = Counter(lst1)
    max_lst = max(count_lst.values())
    mode = [k for k,v in count_lst.items() if v == max_lst]
    
    if max_lst > 1:
        return len(mode)
    else:
        return 0