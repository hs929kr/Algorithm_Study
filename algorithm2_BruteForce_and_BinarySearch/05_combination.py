def combination(numbers,n):
    numbers=list(numbers)
    key=list(range(n))
    limit=list(range(len(numbers)-n,len(numbers)))
    result=[]
    key_loc=n-1
    while(True):   
        arr=[]
        for val in key:
            arr.append(numbers[val])
        arr=''.join(arr)
        result.append(arr)
        key[key_loc]+=1
        if(key[key_loc]>limit[key_loc]):
            while(True):
                if(key[0]>limit[0] and key_loc==0):
                    return result
                if(key[key_loc]>limit[key_loc]):
                    key_loc-=1
                    key[key_loc]+=1
                    if(key[key_loc]<=limit[key_loc]):
                        while(True):
                            key_loc+=1
                            key[key_loc]=key[key_loc-1]+1
                            if(key_loc==n-1):
                                break
                        break
    return result