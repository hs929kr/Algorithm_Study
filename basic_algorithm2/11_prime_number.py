def solution(n):
    answer = 0
    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False
    for i in range(2,n+1):
        if arr[i]==False:
            continue
        for j in range(2*i,n+1,+i):
            arr[j]=False
    for val in arr:
        if val==True:
            answer+=1
    return answer