def solution(s):
    answer = True
    y_num=0
    p_num=0
    for ch in s:
        if ch=='p' or ch=='P':
            p_num+=1            
        if ch=='y' or ch=='Y':
            y_num+=1
    if p_num==y_num:
        return True
    else:
        return False