T = int(input())
# T = 2
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    G = [[0] * N for _ in range(N)]
    E = float(input())
    for n1 in range(N):
        for n2 in range(N):
            G[n1][n2] = E * ((X[n1] - X[n2]) ** 2 + (Y[n1] - Y[n2]) ** 2)
            G[n2][n1] = E * ((X[n1] - X[n2]) ** 2 + (Y[n1] - Y[n2]) ** 2)


    def prim():
        maxv = 10 ** 40
        U = []
        D = [maxv] * N

        D[0] = 0
        while len(U) < N:
            # D에서 최소를 구한다. (단, U에 포함되지 않을 것을 대상으로)
            minV = maxv
            for i in range(N):
                if i in U: continue
                if minV > D[i]:
                    minV = D[i]
                    curV = i
            U.append(curV)
            # i 와 연결된 정점들의 D를 수정
            for i in range(N):
                if i in U: continue
                # if D[i] > D[curV] + dis(curV, i):
                #     D[i] = D[curV] + dis(curV, i)
                if G[curV][i] and D[i] > G[curV][i]:
                    D[i] = G[curV][i]
        print(round(sum(D)))


    print(f'#{tc}', end=' ')
    prim()