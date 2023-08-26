def solution(n):
    answer = 0
    
    ternary = ""
    
    while n > 0 :
        n, mod = divmod(n, 3)
        ternary = ternary + str(mod)
    
    answer = int(ternary, 3)
    
    return answer