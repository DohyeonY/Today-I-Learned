import sys
sys.stdin=open("bus.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    K, N, M = list(map(int, input().split()))
    station = list(map(int, input().split()))
    now = 0
    cnt = 0

    while now + K < N :

        for i in range(K, 0, -1):
            # print(i)
            if now + i in station :
                cnt += 1
                now = now + i
                # print(now)
                break

        # if now + K > N :

        else :
            cnt = 0
            break

    print(f'#{tc} {cnt}')