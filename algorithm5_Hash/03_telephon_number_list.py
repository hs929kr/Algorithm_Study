from collections import deque

def solution(phone_book):
    answer = True    
    phone_book=sorted(phone_book,key=lambda x:x)
    phone_book=deque(phone_book)
    now=phone_book.popleft()
    while(True):
        if(len(phone_book)==0):
            break
        new=phone_book.popleft()
        if(new[0:len(now)]==now):
                answer=False
                break

        now=new
    return answer