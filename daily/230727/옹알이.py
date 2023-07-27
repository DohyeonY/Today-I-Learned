def solution(babbling) :
    answer = 0
    bebe = ['aya', 'ye', 'woo', 'ma']
    not_bebe = ['ayaaya', 'yeye', 'woowoo', 'mama']
    for i in babbling : 
        while i :
            if i[:2] in bebe and i[:4] not in not_bebe :
                i = i[2:]
            elif i[:3] in bebe and i[:6] not in not_bebe :
                i = i[3:]
            else :
                break
        if not i :
            answer += 1
    return answer