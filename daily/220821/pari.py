import sys
sys.stdin=open("pari.txt", "r")

T = int(input())


def sumP(N, M):
    happari = 0

    for ym in range(M):
        for xm in range(M):

            if 0 <= y + M < N and 0 <= x + M < N:
                happari += pan[y + ym][x + xm]


    return happari

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N * N 의 파리판

    pan = [list(map(int, input().split())) for _ in range(N)]

    maxpari = 0
    for y in range(N):
        #
        for x in range(N):
            result = sumP(N,M)
            if result > maxpari:
                maxpari = result

    print(f'#{tc} {maxpari}')
