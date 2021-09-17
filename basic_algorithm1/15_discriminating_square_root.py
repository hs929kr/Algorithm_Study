def solution(n):
    answer = 0
    w=n**(1/2)
    if w==int(w):
        return (w+1)*(w+1)
    else: return -1
    return answer