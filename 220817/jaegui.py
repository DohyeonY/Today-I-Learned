# n! = n*(n-1)!

def factorial(n) :      # 팩토리얼
    if n == 1 :
        return 1
    t = factorial(n-1)
    return n*t

def fibo(n) :           # 피보나취
    if memo[n] == -1 :
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 101
memo[0] = 0
memo[1] = 1

for i in range(101) :
    print(i, fibo(i))

    # if 데이터가 있으면 :
