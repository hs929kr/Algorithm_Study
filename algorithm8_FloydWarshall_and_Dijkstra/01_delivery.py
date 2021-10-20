import sys

def solution(N,road,K):
    answer=0
    cost=[sys.maxsize for i in range(N+1)]
    visited=[False for i in range(N+1)]
    
    cost[0],cost[1],visited[0]=0,0,True
    while(True):
        check=-1
        check_val=sys.maxsize
        for i in range(N+1):
            if visited[i]==False and cost[i]<check_val:
                check=i
                check_val=cost[i]
        if check==-1:
            print(cost)
            print(visited)
            for val in cost:
                if val<=K:      
                    answer+=1
            return answer-1
        visited[check]=True
        for v1,v2,c in road:
            if v1==check and c+cost[v1]<cost[v2]:
                cost[v2]=c+cost[v1]
            if v2==check and c+cost[v2]<cost[v1]:
                cost[v1]=c+cost[v2]
print(solution(N=5,road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],K=3))