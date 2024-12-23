def solution(cipher, code):
    discode = ''.join([vaccine for vaccine in cipher if len(cipher) != 0])
    # if len(cipher) != 0:
    return discode[code-1::code]
    # return answer