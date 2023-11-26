def solution(s):
    lst = s.split(" ")
    result = []
    
    for i in lst :
        result.append(i.capitalize())
        
    return ' '.join(result)