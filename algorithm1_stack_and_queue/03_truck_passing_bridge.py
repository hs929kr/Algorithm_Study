from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=deque([0]*bridge_length)
    truck_weights=deque(truck_weights)
    new=truck_weights.popleft()
    sum_bridge=sum(bridge)
    #divide state as past, now, future apparently!
    #do not use SUM function repeatly for time over
    while(True):
        if(sum_bridge+new-bridge[0]<=weight):
            bridge.append(new)
            out=bridge.popleft()
            sum_bridge=sum_bridge+new-out
            answer+=1
            if(len(truck_weights)!=0):
                new=truck_weights.popleft()
            else:
                new=0
        else:
            bridge.append(0)
            out=bridge.popleft()
            sum_bridge=sum_bridge+0-out
            answer+=1 
        if(len(truck_weights)==0 and sum_bridge==0):
            break
    return answer