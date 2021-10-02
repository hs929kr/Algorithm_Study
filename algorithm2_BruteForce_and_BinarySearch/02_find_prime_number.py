
def is_prime(num):
    if (num<2):
        return False
    limit=int(num**(1/2))    
    for i in range(2,limit+1):
        if(num%i==0):
            return False
    return True      
    
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
                
def permutation(numbers):
    now=[[[]],[list(numbers)]]
    new=[]
    new=[[],[]]
    while(True):
        for i in range(len(now[1])):
            for j in range(len(now[1][0])):
                new_case=list(now[0][i])
                new_case.append(now[1][i][j])
                new[0].append(new_case)
                new[1].append(now[1][i][:j]+now[1][i][j+1:])
        now=new
        new=[[],[]]
        if(now[1][0]==[]):
            for k in range(len(now[0])):
                now[0][k]=''.join(now[0][k])
            break
    return now[0]

def solution(numbers):
    answer = 0
    string_prime=[]
    for i in range(1,len(list(numbers))+1):
        comb=combination(numbers,i)
        for com in comb:
            perm=permutation(com)
            for per in perm:     
                if is_prime(int(per)):
                    string_prime.append(int(per))
    int_prime=set(string_prime)
    answer=len(int_prime)
    
    
    return answer