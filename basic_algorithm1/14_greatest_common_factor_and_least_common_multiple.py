def solution(a, b):
    answer = []
    n=a
    m=b
    mod=n%m
    while(True):
        if mod==0:
            gcd=m
            break
        n=m
        m=mod
        mod=n%m

    lcm=a*b/gcd
    answer.append(gcd)
    answer.append(lcm)
    return answer