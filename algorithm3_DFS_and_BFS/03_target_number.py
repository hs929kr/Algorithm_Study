def dfs(num, arr):
    result=[]
    for i in range(len(arr)):
        result.append(arr[i]+num)
        result.append(arr[i]-num)
    return result
    
numbers=[1,1,1,1,1]
target=3


answer = 0
arr=[0]
for i in range(len(numbers)):
    arr=dfs(numbers[i],arr)
for i in arr:
    if(i==target):
        answer+=1
print(arr)
print(answer)

