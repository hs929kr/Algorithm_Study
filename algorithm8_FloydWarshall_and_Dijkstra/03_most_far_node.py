import sys
import heapq

def solution(n,vertex):
    answer=0
    #rearrangement of array
    vertex_new=[[] for _ in range(n+1)]
    for v1, v2 in vertex:
        vertex_new[v1].append([v2,1])
        vertex_new[v2].append([v1,1])
    vertex=vertex_new

    #heapq, cost initialize
    cost=[sys.maxsize for _ in range(n+1)]
    cost[1]=0
    q=[]
    heapq.heappush(q,(0,1))
    while True:        
        now_cost,now=heapq.heappop(q)
        if now_cost>cost[now]:
            continue
        for new, new_cost in vertex[now]:
            new_cost=now_cost+new_cost
            if cost[new]>new_cost:
                cost[new]=new_cost
                heapq.heappush(q,(new_cost,new))
        if q==[]:
            #print(cost)
            m=max(cost[1:])
            for i in range(n+1):
                if m==cost[i]:
                    answer+=1
            return answer          
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))