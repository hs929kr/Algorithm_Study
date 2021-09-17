def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row=[]
        row1=arr1[i]
        row2=arr2[i]
        for j in range(len(row1)):
            row.append(row1[j]+row2[j])
        answer.append(row)
    return answer