import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
cards=list(map(int,sys.stdin.readline().rstrip().split()))

M=int(sys.stdin.readline().rstrip())
numbers=list(map(int,sys.stdin.readline().rstrip().split()))

counting=dict()
for i in range(N):
    try:
        counting[cards[i]]+=1
    except:
        counting[cards[i]]=1
result=[]
for i in range(M):
    try:
        result.append(counting[numbers[i]])
    except:
        result.append(0)
print(' '.join(map(str,result)))