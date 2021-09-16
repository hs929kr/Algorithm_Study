def solution(n):
    answer = 0
    answer_list=[]
    for i in range(1,n+1):
        if n%i==0:
            answer_list.append(i)
    answer=sum(answer_list)
    return answer