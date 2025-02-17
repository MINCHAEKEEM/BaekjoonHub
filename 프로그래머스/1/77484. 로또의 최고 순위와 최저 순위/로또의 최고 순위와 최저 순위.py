def solution(lottos, win_nums):
    lotto_count = sum(1 for num in lottos if num in win_nums)
    zero_count = lottos.count(0) 
    
    def rank(count):
        if count >= 2:
            return 7 - count
        else: 
            return 6 
    
    return [rank(lotto_count + zero_count), rank(lotto_count)]
