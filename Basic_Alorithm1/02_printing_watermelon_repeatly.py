def solution(n):
    answer = ''
    quotient=n//2
    remainder=n%2
    for i in range(quotient):
        answer=answer+'수박'
    if remainder == 1 :
        answer=answer+'수'
    
    return answer