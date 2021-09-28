def solution(s, n):
    
    answer = ''
    end_lower=ord('z')
    end_upper=ord('Z')
    arr=list(s)
    
    for i in range(len(arr)):
        if(arr[i]==' '):
            continue
        else:
            if(not arr[i].isupper() and end_lower<ord(arr[i])+n):
                arr[i]=chr(ord(arr[i])-(ord('z')-ord('a'))+n-1)
            elif(arr[i].isupper() and end_upper<ord(arr[i])+n):
                arr[i]=chr(ord(arr[i])-(ord('Z')-ord('A'))+n-1)
            else:
                arr[i]=chr(ord(arr[i])+n)
                
    answer=''.join(arr)
    return answer
