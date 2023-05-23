def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    answer += str(0)
    s1 = list(answer)
    s1.reverse()
    for i in range(1,len(s1)):
        answer+=s1[i]


    return answer