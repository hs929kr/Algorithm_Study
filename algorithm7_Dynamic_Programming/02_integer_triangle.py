import sys
from collections import deque

def solution(triangle):
    triangle=deque(triangle)
    now=triangle.popleft()
    if len(triangle)==0:
        return max(now)
    else:
        new=triangle[0].copy()
        for i in range(len(now)):
            val=now[i]
            if triangle[0][i]<new[i]+val:
                triangle[0][i]=new[i]+val
            if triangle[0][i+1]<new[i+1]+val:
                triangle[0][i+1]=new[i+1]+val
        return solution(triangle)
        
        
triangle=[[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
print(solution(triangle))