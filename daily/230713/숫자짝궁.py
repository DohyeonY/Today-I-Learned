def solution(X, Y):
    result = ''
    setx = set(X)
    sety = set(Y)
    i = sorted(setx.intersection(sety), reverse=True)
    s = ''
    for j in i:
        s += str(j) * min(X.count(str(j)), Y.count(str(j)))
    if s and all(n == "0" for n in s):
        s = str(int(s))
    if s != '' :
        result = s
    else :
        result = '-1'
    return result
