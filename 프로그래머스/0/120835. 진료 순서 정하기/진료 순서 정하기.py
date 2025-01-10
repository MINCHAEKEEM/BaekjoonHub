def solution(emergency):
    answer = [0] * len(emergency) # emergency 의 요소를 받아줄 각 초기화 된 리스트 요소를 emergency 길이만큼 생성
    emgc_list = [(lank, emgc) for lank, emgc in enumerate(emergency)] # 순위 정하려면 emergency 인덱스 값이 필요하니까 enumerate 를 사용해서 인덱스와 emergency 요소를 같이 저장한 리스트 생성
    emergency2 = sorted(emgc_list, key = lambda x: x[1], reverse = True) # 순위 정하기 편하게 정렬을 해줄건데 내림차순으로 정렬해줌. 튜플은 리스트랑 정렬방식이 살짝 다르니까 람다로 x(튜플)의 [1]번째 데이터(원 emergency 요소)를 기준으로 내림차순 정렬하라는 기준을 정해줌
    
    for i, (lank,emgc) in enumerate(emergency2): # emergency2 에 대한 인덱스값 i를 불러오기 위해 enumerate를 사용해서 for루프 동작 ex: (i=3의 현순위=맨마지막[2], (0(=3의 원 순위), 3(=원래값)))
        answer[lank] = i+1 # answer 각 요소자리에 원 순위 lank를 넣어주는데, lank의 값은 현순위 i+1임
        
    return answer

# emergency 안의 숫자요소가 높은 순서대로 정렬한 리스트를 반환