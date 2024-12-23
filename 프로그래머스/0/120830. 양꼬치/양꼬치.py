def solution(n, k): # 양꼬치 10인분당 음료수 1개 서비스
                    # 양꼬치는 총 10인분, 64인분 두 경우
    lamb_price = 12000 * n
    drink_price = 2000 * k
    
    if k % 2 != 0: # 음료수 갯수가 n인분과 맞지않으면 추가주문 햇을테니까
        order = drink_price - (2000 * (n//10))
        return lamb_price + order
    else:
        order = drink_price - (2000 * (n//10))
        return lamb_price + order
        
    

# n * 12000
# k * 2000
# service = (2000 * 1) * (n % k)
# total = (n * 12000) + (k * 2000) - service