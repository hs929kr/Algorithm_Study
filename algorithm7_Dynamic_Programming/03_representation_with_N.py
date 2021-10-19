def solution(N,number):
    if N==number:
        return 1
    elif N+N==number or N-N==number or N*N==number or N//N==number or int(str(N)*2)==number:
        return 2
    entire=[[],[N],[N+N,N*N,N//N,int(str(N)*2)]]
    new=[]
    for i in range(3,10):
        if i==9:
            return -1
        for j in range(1,i):
            for p in entire[j]:
                for q in entire[i-j]:
                    if(p//q>0):
                        if(p//q==number):
                            return i
                        new.append(p//q)
                    if(q//p>0):
                        if(p//q==number):
                            return i
                        new.append(q//p)
                    if(p*q==number):
                        return i
                    new.append(p*q)
                    if(p-q>0):
                        if p-q==number:
                            return i
                        new.append(p-q)
                    if(q-p>0):
                        if q-p==number:
                            return i
                        new.append(q-p)
                    if p+q==number:
                        return i
                    new.append(p+q)
        if int(str(N)*i)==number:
            return i
        new.append(int(str(N)*i))
        entire.append(new)
        new=[]
                            
print(solution(3,11))