def solution(k, m, score):
    score = sorted(score)
    answer = 0
    for i in range(len(score)//m):
        for j in range(m-1):
            score.pop()
        answer += score.pop() * m
    return answer