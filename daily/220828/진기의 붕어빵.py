import sys
sys.stdin=open("진기의 붕어빵.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    # print(customer)
    result = 'Possible'
    for i in range(N) :
        boong = (customer[i] // M) * K - (i+1)
        if boong < 0 :
            result = 'Impossible'
            break

    print(f'#{tc} {result}')