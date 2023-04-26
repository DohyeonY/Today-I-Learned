
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


lst = []
N = int(input())
arr = [[0] * N for _ in range(N)]
collst = []
rowlst = []
for _ in range(N) :
    x, y = map(float, input().split())
    lst += (x, y)
for i in range(0, len(lst), 2) :
    collst.append(lst[i])
    rowlst.append(lst[i+1])
for i in range(len(collst)) :
    for j in range(len(collst)) :
        arr[i][j] = ((collst[j] - collst[i]) ** 2 + (rowlst[j] - rowlst[i]) ** 2) ** 0.5
        arr[j][i] = ((collst[j] - collst[i]) ** 2 + (rowlst[j] - rowlst[i]) ** 2) ** 0.5

# print(arr)
# print(prim())
print(f'{prim():.2f}')