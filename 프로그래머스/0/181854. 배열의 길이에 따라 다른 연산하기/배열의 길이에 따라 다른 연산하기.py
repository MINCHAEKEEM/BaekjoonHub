def solution(arr, n):
    for idx in range(len(arr)):
        if len(arr) % 2 == 0:
            if idx % 2 != 0:
                arr[idx] += n
        else:
            if idx % 2 == 0:
                arr[idx] += n

    return arr