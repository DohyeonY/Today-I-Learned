def solution(targets):
    answer = 1
    targets.sort(key = lambda x:x[0])
    
    inner = targets[0]
    
    for i in range(1, len(targets)):
        if inner[1] > targets[i][0]:
            inner = [max(targets[i][0], inner[0]), min(inner[1], targets[i][1])]
        else:
            inner = targets[i]
            answer += 1 
        
    
    return answer