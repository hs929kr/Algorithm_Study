import sys
from collections import deque

#Initialize and make graph
N, M, S=list(map(int,sys.stdin.readline().rstrip().split()))
graph=[]
for i in range(N+1):
    graph.append([])
for i in range(M):
    edge = list(map(int,sys.stdin.readline().rstrip().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    
    
#DFS Implemetation    
DFS_answer=[]
stack=[]
stack.append(S)
visited=[False]*(N+1)
while(stack!=[]):
    now = stack.pop()
    if(visited[now]==False):
        visited[now]=True
        DFS_answer.append(str(now))
    graph[now].sort(reverse=True)
    for i in graph[now]:
        if(visited[i]==False):
            stack.append(i)
print(' '.join(DFS_answer))    

#DFS Implementation
BFS_answer=[]
queue=deque([])
queue.append(S)
visited=[False]*(N+1)
visited[S]=True
while(queue!=deque([])):
    now=queue.popleft()
    BFS_answer.append(str(now))
    graph[now].sort()
    for i in graph[now]:
        if(visited[i]==False):
            queue.append(i)
            visited[i]=True
print(' '.join(BFS_answer))