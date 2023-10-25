def solution(n, a, b):
    result = 0
    
    while a != b :
        result += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
        
    return result
 