def solution(s):
    answer = []
    # print(s)
    word = []
    for i in s :
        wordLen = len(word)
        # print(wordLen)
        if i in word :
            targetIdx = 0
            for j in range(wordLen) :
                if word[j] == i :
                    targetIdx = wordLen - j
            answer.append(targetIdx)
        else : 
            answer.append(-1)
        word.append(i)
        
    # print(answer)
    return answer