def solution(num_str):
    answer = 0
    for num in num_str:
        if num.isdigit():
            answer += int(num)
    return answer