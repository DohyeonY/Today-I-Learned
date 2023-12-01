from collections import deque

def fact(n) :
    if n == 1 :
        return 1
    return n * fact(n - 1)

def solution(n, k):
    answer = []
    deq = deque([i for i in range(1, n + 1)])

    while n > 1 :
        fac = fact(n - 1)
        num = deq[(k - 1) // fac]
        answer.append(num)
        deq.remove(num)
        n -= 1
        k %= fac

    answer.append(deq[-1])
    
    return answer