import sys

def dec_to_bin(N,cnt=1):
    if(N==0):
        return 0
    else:
        h,t=N//2,N%2
        return t*cnt+dec_to_bin(h,cnt*10)

N=int(sys.stdin.readline().rstrip())
sys.stdout.writelines(str(dec_to_bin(N)))
#sys.stdout.writelines(str(bin(N)))