def solution(ingredient):
    result = 0
    burger = []
    
    for i in ingredient :
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1] :
            result += 1
            for j in range(4) :
                burger.pop()
    return result