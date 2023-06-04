def solution(name, yearning, photo):

    result = []
    data = dict(zip(name, yearning))
    
    for i in photo :
        point = 0
        
        for person in i :
            point += data.get(person, 0)
                              
        result.append(point)
    
    return result