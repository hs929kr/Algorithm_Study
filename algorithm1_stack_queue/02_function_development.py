from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days=[]
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    days=deque(days)
    new=days.popleft()
    #must specify about case dividing
    while(True):        
        if(len(days)==0):
            break
        now=new
        cnt=1
        while(True):
            new=days.popleft()
            if(now<new):
                answer.append(cnt)
                if(len(days)==0):
                    answer.append(1)
                break
            else:
                cnt+=1
                if(len(days)==0):
                    answer.append(cnt)
                    break
    return answer