def solution(keymap, targets):
    checker = {}
    answer = []
    for i in keymap :
        for j in range(len(i)) :
            if i[j] not in checker :
                checker[i[j]] = j + 1
            else :
                checker[i[j]] = min(checker[i[j]], j + 1)
    for target in targets :
        count = 0
        for i in target :
            if i not in checker.keys() :
                answer.append(-1)
                break
            else :
                count += checker[i]
        else :
            answer.append(count)
    return answer