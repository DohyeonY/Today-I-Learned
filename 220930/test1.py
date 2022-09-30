def prim():
    U = [False] * N
    D = [1000000000000] * N
    D[0] = 0
    for _ in range(N):
        minV = 1000000000000
        for i in range(N):
            if U[i]: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True

        for i in range(N):
            if U[i]: continue
            if D[i] > arr[curV][i]:
                D[i] = arr[curV][i]

    return sum(D)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lstX = list(map(int, input().split()))
    lstY = list(map(int, input().split()))
    E = float(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                arr[i][j] = 0
            else:
                arr[i][j] = ((lstX[i] - lstX[j]) ** 2 + (lstY[i] - lstY[j]) ** 2) * E

    print(f'#{tc} {round(prim())}')