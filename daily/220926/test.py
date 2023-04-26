dir = [(1,1), (1,-1), (-1,-1), (-1,1)]

def solve(k, r, c, d):
    global maxV

    if d==3 and sr==r and sc==c:
        if maxV < k:
            maxV = k
        return
    
    if d==2 and maxV>=k*2:
        return

    # if r하고 c가 범위를 벗어나거나 같은 디저트면:
    if r<0 or r>=N or c<0 or c>=N or arr[r][c] in result[:k]:
        return
    result[k] = arr[r][c]
    newr, newc = r+dir[d][0], c+dir[d][1]
    solve(k+1, newr, newc, d)
    d = (d+1)%4
    newr, newc = r+dir[d][0], c+dir[d][1]
    solve(k+1, newr, newc, d)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N-2) :
        for j in range(1, N-1) :
            result = [-1] * (4*N)
            sr,sc = i, j
            solve(0, i, j, 0)
    if maxV == 0 :
        print(f'#{tc} -1')
    else :
        print(f'#{tc} {maxV}')