def solution(hp):
    cap_ant_pw = 5
    soldier_ant_pw = 3
    ant_pw = 1
    
    low_hp = hp % cap_ant_pw # 예: 23 % 5 = 3, 24 % 5 = 4
    total_cap_ant = hp // cap_ant_pw # 23 // 5 = 4, 24 // 5 = 4
    total_soldier_ant = low_hp // soldier_ant_pw # 3 // 3 = 1, 4 // 3 = 1
    total_ant = (low_hp % soldier_ant_pw) * ant_pw # (3 % 3) * 1 = 0, (4 % 3) * 1 = 1

    return total_cap_ant + total_soldier_ant + total_ant # 4 + 1 + 0, 4 + 1 + 1

# {장군개미 공격력 : 5, 병정개미 : 3, 일개미 : 1}
# if 체력 23 여치사냥:
#     일개미23마리 == (장군개미4마리 + 병정개미1마리 --> 가성비는 이쪽이 더 좋음)
# 사냥감 체력 변수 hp
# 사냥감 hp에 맞는 ***최소한의 병력 구성*** 을 위한 개미 숫자
# hp는 자연수, 0부터 1000 범위
# 예) hp = 23 : ant = 총 5마리, hp = 24 : ant = 6
# 뭘 해야 하는가
# hp를 ant로 나누고 나머지 계산하기
# 근데 이제 가성비 따져야 하니까 ant의 기본값을 5 라고 생각해야함