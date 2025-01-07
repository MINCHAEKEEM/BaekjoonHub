def solution(rsp):
    answer = ''
    scissors = '2'
    rock = '0'
    paper = '5'
    
    for rsp2 in range(len(rsp)):
        for rsp2 in rsp:
            if scissors in rsp2:
                answer += rock
            elif rock in rsp2:
                answer += paper
            elif paper in rsp2:
                    answer += scissors
        return answer

# 가위 = 2
# 바위 = 0
# 보 = 5