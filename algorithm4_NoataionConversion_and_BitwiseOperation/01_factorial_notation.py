import sys

def Factorial(num):
    answer=1
    while(num!=0):
        answer*=num
        num=num-1
    return answer
def F_notation_to_decimal(num):
    answer=0
    num=list(map(int,list(str(num))))
    N=len(num)
    for i in num:
        answer+=i*Factorial(N)
        N-=1
    return answer
        

while(True):
    num=int(sys.stdin.readline().rstrip())
    if(num==0):
        break
    else:
        decimal=F_notation_to_decimal(num)
        print(decimal)