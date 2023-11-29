def solution(prices):
    answer = [0 for i in range(len(prices))]
    
    for i in range(len(prices)) :
        for j in range(i + 1, len(prices)) :
            answer[i] += 1
            
            if prices[i] > prices[j] :
                break
        
    return answer