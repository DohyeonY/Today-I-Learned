def solution(n, l, r):
    if n == 0 :
        return 1
    if l > 1 :
        return solution(n, 0, r) - solution(n, 0, l - 1)
    if r <= 5 ** (n - 1) :
        return solution(n - 1, l, r)
    elif r <= 2 * 5 ** (n - 1) :
        return 4 ** (n - 1) + solution(n - 1, l, r - 5 ** (n - 1))
    elif r <= 3 * 5 ** (n - 1) :
        return 4 ** (n - 1) * 2
    elif r <= 4 * 5 ** (n - 1) :
        return 4 ** (n - 1) * 2 + solution(n-1, l, r - 5 ** (n - 1) * 3)
    else :
        return 4 ** (n - 1) * 3 + solution(n - 1, l, r - 5 ** (n - 1) * 4)
    
    return 4 ** n