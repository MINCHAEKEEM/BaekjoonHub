def solution(sides):
    in_max = max(sides)
    total_sum = sum(sides)
    minusdata = total_sum - in_max
    
    if in_max > minusdata:
        return 2
    elif in_max < minusdata:
        return 1
    else:
        return 2

    