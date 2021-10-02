from collections import deque
#it is important understaing proble correctly                             
def solution(prices):
    answer = []    
    prices=deque(prices)
    while(len(prices)!=0):
        t=0
        now=prices.popleft()
        for val in prices:
            if(now>val):
                t+=1
                break
            t+=1
        answer.append(t)
    return answer