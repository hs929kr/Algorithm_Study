import sys

def N_notation_to_deciaml(num,N):
    if(N>10):
        answer=0
        std=ord('A')
        num=list(num)
        length=len(num)
        for val in num:
            length-=1
            try:
                answer+=(N**length)*int(val)
            except:
                answer+=(N**length)*(ord(val)-std+10)
        return answer
    elif(N<10):
        answer=0
        num=list(num)
        length=len(num)
        for val in num:
            length-=1
            answer+=(N**length)*int(val)
        return answer
    else:
        answer=int(num)
        return answer
    
num=sys.stdin.readline().rstrip().split()
answer=N_notation_to_deciaml(num[0],int(num[1]))
sys.stdout.write(str(answer))