def solution(x):
    answer = True
    nx=list(map(int,list(str(x))))
    if x%sum(nx)==0:
        answer=True
    else:
        answer=False
    return answer