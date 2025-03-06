def solution(numbers, n):
    num_box = 0
    
    while num_box <= n:
        for num in numbers:
            num_box += num
            if num_box > n:
                return num_box