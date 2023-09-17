def solution(want, number, discount):
    answer = 0
    lst = []
    
    for i, j in zip(want, number) :
        lst += [i] * j
        
    lst = sorted(lst)
    
    for k in range(len(discount[:-len(lst) + 1])) :
        answer += int(lst == sorted(discount[k : len(lst) + k]))
        
    return answer