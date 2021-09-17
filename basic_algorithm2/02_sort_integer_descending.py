def solution(n):
    answer = 0
    arr=list(map(int,list(str(n))))    
    arr.sort()
    arr.reverse()
    arr=list(map(str,arr))
    charr=''
    for i in arr:
        charr+=i
    answer=int(charr)
    return answer