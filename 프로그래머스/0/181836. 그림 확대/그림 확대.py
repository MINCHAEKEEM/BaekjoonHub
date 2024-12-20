def solution(picture, k): # 그림크기 1*1 픽셀그림의 k배 늘린 값 구하기 
    # 1. 가로 방향으로 k배 확대
    width = []
    for pic in picture:
        pic2 = []
        for p in pic:
            pic2.append(p * k)
        width.append(''.join(pic2))
        # width = [''.join(p * k for p in pic) for pic in picture]
    
    # 2. 세로 방향으로 k배 확대
    result = []
    for pic in width:
        result.extend([pic] * k)
    
    return result

# 그림크기 1*1 픽셀그림의 k배 늘린 값 구하기
#     a = ''.join(picture) 
    
#     m = [i * k for i in a]
#     m1 = m[0:3]
#     m2 = m[3:6]
#     m3 = m[6:]
#     g1 = ''.join(m1)
#     g2 = ''.join(m2)
#     g3 = ''.join(m3)
#     return ([g1] * k) + ([g2] * k) + ([g3] * k)