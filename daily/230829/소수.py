def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1) :
        c, j = 0, 1

        while j <= i :
            if i % j == 0 :
                c += 1
            j += 1
            
        if c % 2 == 0 :
            answer += i
        else:
            answer -= i
            
    return answer