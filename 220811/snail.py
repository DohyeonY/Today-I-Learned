arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,23,24,25]

def selection(value) :
    miny = 100000000000
    resultR, resultC = 0, 0
    for row in range(N) :
        for col in range(N):
            if value < arr[row][col] < miny :
                miny = arr[row][col]
                resultR, resultC = row,col

    return resultR, resultC


# 오, 아, 왼, 위

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
curR, curC = 0, 0
N = 5

d = 0
check = [[False] * N for _ in  range(N)]
d = 0
value = 0
for i in range(N*N) :
    (idxR, idxC) = selection(value)
    value = arr[idxR][idxC]
    arr[curR][curC], arr[idxR][idxC] = arr[idxR][idxC], arr[curR][curC]
    check[curR][curC] = True
    newR = curR + dr[d]
    newC = curC + dc[d]

    if newR<0 or newR >= N or newC<0 or newC >= N or check[newR][newC] :
        d = (d +1) % 4

    curR = curR + dr[d]
    curC = curC + dc[d]

print(arr)
