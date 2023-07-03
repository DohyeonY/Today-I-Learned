def solution(a, b,ｎ):
    result = 0
    while n >= a :
        result += (n // a) * b
        n = (n % a) + (n // a)*b
    return result