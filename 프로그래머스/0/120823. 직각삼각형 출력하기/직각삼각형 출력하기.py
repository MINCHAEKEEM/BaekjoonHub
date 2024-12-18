n = int(input())
star = '*'
widthheight = 1 * 1
WH = widthheight

for s in range(1, n+1):
    s = star * WH
    WH += 1    
    print(s)