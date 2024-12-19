def solution(my_string, n):
    answer = ''
    for s in range(n):
        s = my_string
        a = [s * n for s in my_string]
        return ''.join(a)