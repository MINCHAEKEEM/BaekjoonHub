def solution(s):
    return ''.join(sorted(s, reverse=True, key=lambda x: (x.islower(), x)))