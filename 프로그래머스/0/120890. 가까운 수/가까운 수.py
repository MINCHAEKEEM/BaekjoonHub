def solution(array, n):
    # 배열을 정렬합니다.
    array.sort()
    
    # 각 요소와 n의 차이를 계산한 결과를 기준으로 정렬합니다.
    # 차이가 같을 경우 더 작은 수가 우선시됩니다.
    return min(array, key=lambda x: (abs(x - n), x))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # my_list = [n - arr if n > arr else arr - n for arr in array]
    # answer = 0
    # if len(my_list) !=0:
    #         new_dict = {key : value for key, value in zip(array,my_list)}
    # if min(new_dict.values()) == min(my_list):
    #     answer += max(new_dict.keys())
    # print(min(new_dict.values()))
    # return answer

# 어레이에 들어있는 정수 중에 n과 가장 가까운 수를 반환
# 대신 가까운 수가 여러 개 일 경우 제일 가까운 수를 반환