def solution(clothes):
    answer = 1
    c = {v[1] : [] for  v in clothes}
    
    for cloth in clothes :
        c[cloth[1]].append(cloth[0])
    
    for i in c.keys() :
        answer *= (len(c[i]) + 1)
        
    return answer - 1