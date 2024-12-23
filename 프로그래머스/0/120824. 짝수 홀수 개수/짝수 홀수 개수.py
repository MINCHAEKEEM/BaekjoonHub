def solution(num_list):
    even_count = 0
    odd_count = 0
    # even_count = sum(1 for num in num_list if num % 2 == 0)  # 짝수 개수 세기
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
            
    # odd_count = sum(1 for num in num_list if num % 2 != 0)   # 홀수 개수 세기
        else:
            odd_count += 1
    return [even_count, odd_count]