import sys

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
    
N=int(sys.stdin.readline().rstrip())
answer=factorial(N)
sys.stdout.writelines(str(answer))