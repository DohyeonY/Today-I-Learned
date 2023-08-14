def solution(d, budget):
    
    answer = 0
    
    d.sort(reverse = False)
    
    for i in d:
        
        if budget-i < 0 :
            break
        
        else:
            answer += 1
            budget -= i
    
    return answer