def solution(arr):
    arr_num = []
    binmunja = ''
    x = []
    for a in str(arr):
        if a.isdigit():
            arr_num.append(a * int(a))
    for num in arr_num:
        if num != 0:
            binmunja += num
            x.append(num)
            binmunja = ''
    return x