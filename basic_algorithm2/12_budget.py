def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget=budget-d[i]
        if(budget<0):
            answer=i
            break
        if(i==len(d)-1):
            answer=len(d)
    return answer