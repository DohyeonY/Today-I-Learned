def solution(order):
    answer = 0
    box = list(range(1, len(order) + 1))
    aux = []
    i, j = 0, 0   
    
    while j < len(order) :
        if aux and aux[-1] == order[j] :
            aux.pop()
            j += 1
            answer += 1
            continue
            
        while box[i] < order[j] :
            aux.append(box[i])
            i += 1

        if box[i] != order[j] and aux[-1] != order[j] :
            break
        
        elif box[i] == order[j] :
            answer += 1
            i += 1
            j += 1
            
    return answer