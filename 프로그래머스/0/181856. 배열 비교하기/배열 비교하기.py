def solution(arr1, arr2):
    answer = 0
    while len(arr1) > len(arr2):
        answer += 1
        break
    while len(arr1) < len(arr2):
        answer += -1
        break
    while len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2): 
            answer += 1
            break
        elif sum(arr1) < sum(arr2):
            answer += -1
            break
        elif sum(arr1) == sum(arr2):
            answer
            break
    
    return answer