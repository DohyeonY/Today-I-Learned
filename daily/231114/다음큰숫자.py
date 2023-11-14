def solution(n):
    
    cnt = bin(n)[2:].count("1")
    
    while True :
        n += 1
        if cnt == bin(n)[2:].count("1") :
            break

    return n