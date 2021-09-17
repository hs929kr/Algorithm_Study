def solution(arr, divisor):
    answer = []
    for val in arr:
        if(val%divisor==0):
            answer.append(val)
    if(answer==[]):
        answer.append(-1)
    else:
        answer.sort()
    return answer