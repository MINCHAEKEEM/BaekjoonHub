def solution(message): 
    a = [msg for msg in message]
    # for msg in message:
    #     a.append(msg)
    if len(a) != 0:
        return len(a) * 2



# 편지지 가로길이 구하기
# 필요한것: 메시지의 길이
# 가로길이 = 메시지요소 * 2