def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    answer = ''
    letter2 = letter.split()
    for l in letter2:
        if l in morse:
            answer += morse.get(l)
    return answer

# morse 의 내용을 토대로 letter의 내용을 영어 소문자로 바꾼 문자열 반환