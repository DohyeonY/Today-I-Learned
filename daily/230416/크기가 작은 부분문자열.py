def solution(t, p):
    answer = 0
    
    res = ""
    for i in t :
        res += i
        
        if len(res) == len(p) :
            if int(res) <= int(p) :
                answer += 1
                
            res = res[1:]
    return answer