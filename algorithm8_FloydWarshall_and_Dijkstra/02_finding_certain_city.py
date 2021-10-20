import sys
import heapq

def solution(city_num,road_num,K,start,road_info):
    m_cnt=0
    #road initializtion
    new_road_info=[[] for _ in range(city_num+1)]
    for v1, v2 in road_info:
        new_road_info[v1].append([v2,1])
    road_info=new_road_info
    #cost, heap initailization
    cost=[sys.maxsize for _ in range(city_num+1)]
    cost[1]=0
    q=[]
    heapq.heappush(q,(0,start))
    while True:
        now_val,now=heapq.heappop(q)
        if now_val>cost[now]:
            continue
        for new,new_val in road_info[now]:
            new_val=new_val+now_val
            if new_val<cost[new]:
                cost[new]=new_val
                heapq.heappush(q,(new_val,new))
        if q==[]:
            #print(cost)
            for i in range(1,len(cost)):
                if cost[i]==K:
                    print(i)
                    m_cnt+=1
            if m_cnt==0:
                print(-1)
            return
city_num,road_num,K,start=list(map(int,sys.stdin.readline().rstrip().split()))
road_info=[]
for i in range(road_num):
    road_info.append(list(map(int,sys.stdin.readline().rstrip().split())))
solution(city_num,road_num,K,start,road_info)