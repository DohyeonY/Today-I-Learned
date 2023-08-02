def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    po1 = [1, 2, 3, 4, 5]
    po2 = [2, 1, 2, 3, 2, 4, 2, 5]
    po3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)) :
        if answers[i] == po1[i % (len(po1))] :
            cnt[0] += 1
        if answers[i] == po2[i % (len(po2))] :
            cnt[1] += 1
        if answers[i] == po3[i % (len(po3))] :
            cnt[2] += 1
    
    for i in range(len(cnt)) :
        if cnt[i] == max(cnt) :
            answer.append(i + 1)
    return answer