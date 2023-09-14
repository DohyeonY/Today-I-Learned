def solution(elements):
    answer = set()
    
    for i in range(1, len(elements)) :
        sums = elements + elements[: i - 1]
        
        for j in range(len(sums) - (i - 1)) :
            answer.add(sum(sums[j : j + i]))
    
    answer.add(sum(elements))
    
    return len(answer)