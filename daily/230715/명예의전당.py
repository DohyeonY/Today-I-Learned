def solution(k, score):
    answer = []

    for i in range(len(score)) :
        rank = sorted(score[0 : i + 1], reverse = True)

        if i >= k :
            answer.append(rank[k-1])

        else:
            answer.append(min(rank))
            
    return answer