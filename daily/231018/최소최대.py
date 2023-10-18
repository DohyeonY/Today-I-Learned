def solution(s):
    answer = ''
    s = list(map(int, s.split(' ')))
    s.sort()
    min = s.pop(0)
    max = s.pop()
    
    return str(min) + ' ' + str(max)