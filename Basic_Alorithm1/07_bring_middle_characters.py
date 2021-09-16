def solution(s):
    answer = ''
    quotient=len(s)//2
    remainder=len(s)%2
    if remainder==0:
        answer=s[quotient-1:quotient+1]
    else:
        answer=s[quotient]
    return answer