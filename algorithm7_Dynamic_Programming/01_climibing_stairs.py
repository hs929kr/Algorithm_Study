import sys

stairs=[]
values=[]
max_val=0
def sol(sum=0, index=0,limit=-1):
    global stairs
    global N
    global max_val
    global check
    if index>N-1:
        return
    elif index==N-1:
        sum+=stairs[index]
        if max_val>=sum:
            return
        else:
            max_val=sum
        return
    else:
        sum+=stairs[index]
        if limit==1:#이전에 한칸
            if check[index][0]<sum:
                check[index][0]=sum
                sol(sum,index+2,limit=0)#이전에 두칸
            else:
                return
        elif limit<1:
            if limit==-1:
                sol(sum,index+1,limit+1)
                sol(sum,index+2,limit=0) 
            else: 
                if check[index][1]<sum:
                    check[index][1]=sum
                    sol(sum,index+1,limit+1)
                    sol(sum,index+2,limit=0)
                else:
                    return

N=int(sys.stdin.readline().rstrip())
check=[[0 for i in range(2)] for j in range(N)]
stairs.append(0)
for i in range(N):
    stairs.append(int(sys.stdin.readline().rstrip()))
N=N+1
sol()
sys.stdout.writelines(str(max_val))