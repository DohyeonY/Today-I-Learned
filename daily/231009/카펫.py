def solution(brown, yellow):
    answer = []
    s = brown + yellow
    
    for i in range(1, s) :
        if s % i == 0 :
            a = s // i
            
            if i < a :
                i, a = a, i
                
            if yellow == s - (2 * i + 2 * a - 4) :
                
                return  [i, a]