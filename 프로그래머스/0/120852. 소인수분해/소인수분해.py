import math
def solution(n):
    answer = []

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            answer.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        answer.append(n)
        
    return answer

# def solution(n):
#     answer = []
    
#     x = 2
#     while x <= n:
#         if n % x == 0:
#             if x not in answer:
#                 answer.append(x)
#             n //= x
#         else:
#             x += 1
#     return answer