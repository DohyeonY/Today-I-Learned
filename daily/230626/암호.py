def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip :
        alpha = alpha.replace(i, '')
    for j in s :
        change = alpha.find(j) + index
        while change >= len(alpha) :
            change -= len(alpha)
        answer += alpha[change]
    return answer