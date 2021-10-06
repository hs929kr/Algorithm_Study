
import sys
def new_hash(n,key):
    key=list(key)
    answer=0
    r=0
    for i in range(n):
        val=ord(key[i])-ord('a')+1
        answer+=val*(31**r)
        r=r+1
    answer=answer%1234567891
    return answer
    
N=int(sys.stdin.readline().rstrip())
key=sys.stdin.readline().rstrip()
print(new_hash(N,key))