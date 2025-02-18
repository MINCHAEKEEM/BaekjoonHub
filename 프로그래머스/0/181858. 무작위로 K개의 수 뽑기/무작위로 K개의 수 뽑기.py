def solution(arr, k):
    unique_nums = list(dict.fromkeys(arr))  # 중복을 제거하면서 원래 순서 유지
    answer = unique_nums[:k]  # k개까지만 자르기

    while len(answer) < k:  # k보다 작으면 -1 추가
        answer.append(-1)

    return answer
