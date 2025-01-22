import re
def solution(s):
    answer = []
    num = []
    new_s = s.split()
    pattern = r"^-?\d+(\.\d+)?([eE][-+]?\d+)?$"
    
    for i in new_s:
        if re.match(pattern, i):
            num.append(int(i))
        else:
            if num:
                num.remove(num[-1])
                answer.extend(num)
                num = []
    if num:
        answer.extend(num)

    result = sum(answer)
    return result

# s 안에 있는 숫자를 더한 값 반환하기
# 근데 이제 Z를 만났을 땐 바로 전에 더했던 숫자값을 빼야함