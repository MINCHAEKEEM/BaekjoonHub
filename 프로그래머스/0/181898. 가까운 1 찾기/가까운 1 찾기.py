def solution(num_list, idx):
    for i in range(idx, len(num_list)):
        if num_list[i] == 1:
            return i
    else: # 반복문이 끝날 때까지 1이 안나오면
        return -1