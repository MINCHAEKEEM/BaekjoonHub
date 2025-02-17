def solution(common):
    if common[1] - common[0] == common[2] - common[1]: 
        gongcha = common[1] - common[0]
        return common[-1] + gongcha
    else: 
        gongb = common[1] / common[0]
        return common[-1] * int(gongb)

