import sys
sys.stdin=open("strange.txt", "r")


primes = [False, False] + [True] * 1000000
def general(A, B) :
    for num in range(A, B+1):
        if primes[num] == True :
            for idx in range(num+num, B+1, num) :
                primes[idx] = False
        # for j in range(2, int(num**0.5)-1) :
        #     if num % j == 0 :
        #         break
        #         # prinmes[num] = False
        # else :
        #     primes[num] = True


T= int(input())

for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    general(A,B)
    cnt = 0
    for idx in range(A, B+1) :
        if primes[idx] and str(D) in str(idx) :
            cnt += 1

    print(f'#{tc} {cnt}')