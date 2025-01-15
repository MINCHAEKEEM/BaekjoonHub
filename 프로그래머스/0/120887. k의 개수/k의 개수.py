def solution(i, j, k):
    answer = 0
    # i부터 j까지 숫자들을 문자열로 합침
    numbers = ''.join(map(str, range(i, j + 1)))
    # k를 문자열로 변환한 뒤, 문자열에서 등장 횟수 계산
    return numbers.count(str(k))
    # for num in range(i,j+1):
    #     for k1 in range(k+1):
    #         if str(k) in str(num):
    #             answer += 1
    #             if str(k) in str(num) and (num - k) % k == 0:
    #                 answer += 1
    # print(str(k),'k')
    # print(str(num),'num')
    # print(str(answer),'answer')
    # return answer

# i부터 j까지 k가 몇 번 등장하는지를 반환
# 포문
# 레인지를 j번 돌려야하나?

