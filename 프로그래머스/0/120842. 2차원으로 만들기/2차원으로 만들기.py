def solution(num_list, n):
    answer = [num_list[num * n : (num + 1) * n] for num in range((len(num_list)//n))] 
    # answer = []
    # for num in range((len(num_list)//n)):
    #     if n != 0:
    #         answer.append(num_list[num * n : (num + 1) * n])
    return answer


# 넘리스트 길이 8에 엔이 2면 넘리스트의 요소들을 두개씩 잘라묶은 이차원 배열 반환
# 일단 포문 실행해보기
# 넘리스트의 길이만큼 레인지해보기
# 이프 조건문에 넘리스트 렌 나누기 엔이 영과 같을 때 엔씩 앤서에 추가하기 조건 달아보기 >> 엔이 홀수일 경우도 있기 때문에 엔이 영이 아니라면 조건으로 수정해봄
# 이차원 앤서에 추가하기가 애매할거같으면 앤서는 1차원 리스트로, 중간에 빈 리스트 만들어서 해보기
# 이차원 앤서를 빈 리스트로 바꾸고, 넘리스트 길이만큼의 [0] 리스트 만들어보기