def binary_to_wall(binary):
    for i in range(len(binary)):
        if(binary[i]==1):
            binary[i]="#"
        else:
            binary[i]=' '
    wall=''.join(binary)
    return wall

def integer_to_binary(integer,n):
    bina=[]
    for i in range(n):
        residual=integer%2
        integer=integer//2
        bina.append(residual)
    return bina
def solution(n, arr1, arr2):
    answer = []
    arr3=[]
    for i in range(n):
        arr=[]
        arr1_line=binary_to_wall(integer_to_binary(arr1[i],n))
        arr2_line=binary_to_wall(integer_to_binary(arr2[i],n))
        for j in range(n):
            if(list(arr1_line)[j]=="#" or list(arr2_line)[j]=="#"):
                arr.append("#")
            else:
                arr.append(' ')
        arr3.append(''.join(reversed(arr)))
    answer=arr3
    return answer
