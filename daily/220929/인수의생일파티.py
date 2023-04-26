import sys
sys.stdin=open("인수의생일파티.txt")

def dijk(G):
    U = [False] * (N + 1)
    D = [999999999999999] * (N + 1)
    D[X] = 0
    while U.count(True) < N:
        minV = 999999999999999
        for i in range(N + 1):
            if U[i]: continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        U[curV] = True
        for i in range(N + 1):
            if U[i]: continue
            D[i] = min(D[i], D[curV] + G[curV][i])
    return D


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    G1 = [[999999999999999] * (N + 1) for _ in range(N + 1)]
    G2 = [[999999999999999] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        G1[x][y] = c
        G2[y][x] = c
    D1 = dijk(G1)
    D2 = dijk(G2)
    maxV = -1
    for i in range(N + 1):
        sumV = D1[i] + D2[i]
        if sumV != 2 * 999999999999999:
            maxV = max(sumV, maxV)

    print(f'#{tc} {maxV}')
