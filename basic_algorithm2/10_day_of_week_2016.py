def solution(a, b):
    answer = ''
    week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    months=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    sum_dates=sum(months[0:a])
    answer=week[(sum_dates+b)%7-1]
    return answer