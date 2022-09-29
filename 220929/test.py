def prim() :
    U = []
    D = [1000000] * (N+1)
    D[0] = 0
    while len(U) < N+1 :
        # D에서 최소를 구한다.(단. U에 포함되지 않은 것을 대상으로)
        minV = 1000000
        for i in range(N+1) :
            if i in U : continue
            if minV > D[i] :
                minV = D[i]
                curV = i

        U.append(curV)
        # i와 연결된 정점들의 D를 업데이트
        for i in range(N+1) :
            if i in U : continue
            if G[curV][i] and D[i] > G[curV][i] :
                D[i] = G[curv][i]
                P[i] =


N, E = map(int, input().split())
G = [[0] for _ in range(N+1)]
for i in range(E) :