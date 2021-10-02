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