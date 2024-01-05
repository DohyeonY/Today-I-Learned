import itertools

def solution(numbers):
    answer = set()
    combi = list(itertools.combinations(numbers, 2))
    
    for a, b in combi:
        answer.add(a+b)
        
    result = sorted(list(answer))
    
    return result