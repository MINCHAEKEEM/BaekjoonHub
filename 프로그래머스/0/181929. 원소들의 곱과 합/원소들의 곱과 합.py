def solution(num_list):
    product = 1          # 모든 원소의 곱을 저장할 변수 (초기값 1)
    total = 0            # 모든 원소의 합을 저장할 변수 (초기값 0)
    
    # 리스트의 모든 원소에 대해 곱과 합을 계산
    for num in num_list:
        product *= num
        total += num
    
    # 모든 원소의 곱이 합의 제곱보다 작으면 1, 그렇지 않으면 0 반환
    return 1 if product < total ** 2 else 0















# def solution(num_list):
#     answer = 0
#     num_mul = multiply()
#     num_sum = pow(sum(num_list), 2)
    
#     for num in num_list:
#         num_box *= num
#     if num_box < num_sum:
#         answer += 1
#     else:
#         answer
#     print(num_box)
#     print(num_sum)
#     return answer