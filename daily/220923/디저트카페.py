import sys
sys.stdin=open("디저트카페.txt", "r")

def solve(k, r, c, d):
    global maxV

    if d == 3 and r == stR and c == stC :
        if maxV < k :
            maxV = k
        return
    if d == 2 and maxV >= k * 2
        return
    if r < 0 or r >= N or c < 0 or c >= N or arr[r][c] in result[:k] :
        return

    result[k] = arr[r][c]
    newR, newC =
    solve(k+1, newR, newC, d)
    d = (d+1)%
    newR, newC =
    solve(k+1, newR, newC, d)



T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    maxV = 0
    for r in range(N) :
        for c in range(N) :
            stR, stC = r, c
            result = [-1] * (4*N)
            solve(0, r, c, 0)