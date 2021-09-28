def solution(n, lost, reserve):
    answer = 0
    arr=(n+2)*[1]
    lost.sort()
    reserve.sort()
    for i in reserve:
        arr[i]=2
    for i in lost:
        if(arr[i]==2):
            arr[i]=1
        elif(arr[i]==1):
            arr[i]=0
    
    for i in reserve:
        if(arr[i]==2 and arr[i-1]==0):
            arr[i-1]=1
            arr[i]=1
        elif(arr[i]==2 and arr[i+1]==0):
            arr[i+1]=1 
            arr[i]=1
            
    for val in arr:
        if(val==1 or val==2):
            answer+=1
            
    answer=answer-2
    return answer