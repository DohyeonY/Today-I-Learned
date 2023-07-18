def dtd(date) :
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    
    today = dtd(today)
    for i in range(len(privacies)) :
        sd, type = privacies[i].split()
        sd = dtd(sd)
        for term in terms :
            ftype, fterm = term.split()
            if ftype == type and sd + (int(fterm) * 28) <= today :
                answer.append(i + 1)
    return answer