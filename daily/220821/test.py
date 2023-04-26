import sys
sys.stdin=open("ruins.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0

    for row in range(N):
        cnt = 0
        for col in range(M):
            if arr[row][col] == 1:
                cnt += 1
                if cnt > maxV:
                    maxV = cnt
            else:
                cnt = 0

    for col in range(M):
        cnt = 0
        for row in range(N):
            if arr[row][col] == 1:
                cnt += 1
                if cnt > maxV:
                    maxV = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxV}')