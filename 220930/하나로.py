
import sys
sys.stdin=open('하나로.txt')

def distance(x1, y1, x2, y2) :
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def prim() :
    U = [False] * N
    D = [999999999999999] * N
    D[0] = 0

    for _ in range(N) :
        result = 999999999999999999

        for i in range(N) :
            if U[i] : continue
            if result > D[i] :
                result = D[i]
                curV = i
        U[curV] = True
        # U.append(curV)
        for i in range(N) :
            if U[i] : continue
            if D[i] > arr[curV][i] :
                D[i] = arr[curV][i]
            # if D[i] > D[curV] + dis(curV, i) :
            #     D[i] = D[curV] + dis(curV, i)
    return sum(D)

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    collst = list(map(int, input().split()))
    rowlst = list(map(int, input().split()))
    tax = float(input())
    arr = [[0] * N for _ in range(N)]
    # print(arr)
    for i in range(N) :
        for j in range(N) :
            arr[i][j] = tax * distance(collst[i], rowlst[i], collst[j], rowlst[j])
            arr[j][i] = tax * distance(collst[i], rowlst[i], collst[j], rowlst[j])
    # print(arr)

    print(f'#{tc} {round(prim())}')