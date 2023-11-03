def solution(n):
    answer = hanoi(n, 1, 3, 2)  
    
    return answer

def hanoi(num, start, end, bypass):
    if num == 1 :
        return [[start, end]]
    
    else:
        path = []
        path += hanoi(num - 1, start, bypass, end)
        path += [[start, end]]
        path += hanoi(num - 1, bypass, end, start)
        
        return path