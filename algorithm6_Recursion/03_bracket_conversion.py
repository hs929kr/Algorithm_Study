import sys

def solution(v):
    front_num,back_num=0,0
    if len(v)==0:
        return ''
    else:
        for i in range(len(v)):
            if v[i]=='(':
                front_num+=1
            else:
                back_num+=1
            if front_num==back_num:
                u=v[:i+1]
                v=v[i+1:]
                break
        if u[0]==')':
            u=u[1:-1]
            new_u=''
            for i in range(len(u)):
                if u[i]=='(':
                    new_u=new_u+')'
                else:
                    new_u=new_u+'('
            return '('+solution(v)+')'+new_u
        else:
            return u+solution(v)

S=sys.stdin.readline().rstrip()
sys.stdout.writelines(solution(S))