def solution(array):
    answer = 0
    answer = array
    sorted_data = sorted(answer)
    n = len(sorted_data)
    
    if n % 2 == 0:
        return (sorted_data[n//2 -1] + sorted_data[n//2] / 2)
    else:
        return sorted_data[n//2]
  