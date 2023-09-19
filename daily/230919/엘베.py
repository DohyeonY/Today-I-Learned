def solution(storey):
    answer = 0
    while storey != 0 :
        answer += (storey % 10 if 5 > storey % 10 else 10 - storey % 10)
        if (storey % 10 == 5 and storey % 100 >= 50) or (storey % 10 > 5):
            storey += 10
        storey //= 10
    return answer