def solution(n, a, b) :
    result = 0
    
    while a != b :
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        result += 1
        
    return result