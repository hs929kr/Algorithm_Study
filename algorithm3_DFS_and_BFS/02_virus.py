import sys

#make graph
computers=int(sys.stdin.readline().rstrip())
line_num=int(sys.stdin.readline().rstrip())
graph=[]
for i in range(computers+1):
    graph.append([])
for i in range(line_num):
    line=list(map(int,sys.stdin.readline().rstrip().split()))
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])
#DFS
result=0
stack=[]
stack.append(1)
visited=[False]*(computers+1)
while(stack!=[]):
    now=stack.pop()
    if(visited[now]==False):
        visited[now]=True
        result+=1
    for com in graph[now]:
        if(visited[com]==False):
            stack.append(com)
print(result-1)