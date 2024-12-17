def solution(price):
    answer = 0
        
    if price in range(100000, 300000):
        return int(price - (price * 0.05))
    elif price in range(300000, 500000):
        return int(price - (price * 0.1))
    elif price >= 500000:
        return int(price - (price * 0.2))
    else:
        return price
        
   