def solution(money):
    americano = 5500
    cup = money // americano
    return [cup, money - (cup * americano)]
    