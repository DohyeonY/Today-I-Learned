def solution(citations):
    citations.sort()
    
    for i , citation in enumerate(citations) :
        if citation >= len(citations) - i :
            return len(citations) - i
    return 0