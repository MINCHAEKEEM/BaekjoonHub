def solution(rny_string):
    mystr = ''

    for rny_str in rny_string:
        if rny_str == 'm':
            my_str = rny_str.replace('m', 'rn')
            mystr += my_str
        else:
            mystr += rny_str

    return mystr