def solution(answers):
    answer =[]
    patternA=[1,2,3,4,5]
    patternB=[2,1,2,3,2,4,2,5]
    patternC=[3,3,1,1,2,2,4,4,5,5]
    
    numA=0
    numB=0
    numC=0
    A=patternA*(len(answers)//len(patternA))
    B=patternB*(len(answers)//len(patternB))
    C=patternC*(len(answers)//len(patternC))
    
    for i in range(len(answers)%len(patternA)):
        A.append(patternA[i])
    for i in range(len(answers)%len(patternB)):
        B.append(patternB[i])
    for i in range(len(answers)%len(patternC)):
        C.append(patternC[i])
    
    for i in range(len(answers)):
        if A[i]==answers[i]:
            numA+=1
        if B[i]==answers[i]:
            numB+=1
        if C[i]==answers[i]:
            numC+=1
    
    total=[numA,numB,numC]
    max_val=max(total)
    for i in range(3):
        if(total[i]==max_val):
            answer.append(i+1)
    
    return answer