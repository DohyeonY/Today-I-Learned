def solution(n):
    dic = {}
    
    dic[0] = 1
    dic[1] = 1
        
    for i in range(2, n + 1) :
        dic[i] = dic[i - 1] + dic[i - 2]
    
    answer = dic[n] % 1234567    
    
    return answer