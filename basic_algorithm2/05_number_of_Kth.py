def solution(array, commands):
    answer = []
    for command in commands:
        new_array=array[command[0]-1:command[1]]
        new_array.sort()
        result=new_array[command[2]-1]
        answer.append(result)
    
    return answer