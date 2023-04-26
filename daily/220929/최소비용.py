from collections import deque

def solve() :
    Q = deque()
    Q.append((0, 0))
    dis[0][0] = 0
    while Q :
        row, col = Q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] :
            newR, newC = row + dy, col + dx
            if 0 <= newR < N and 0<= newC < N :
                gap = max(arr[newR][newC] - arr[row][col], 0) + 1
                if dis[newR][newC] > dis[row][col] + gap :
                    dis[newR][newC] = dis[row][col] + gap
                    Q.append((newR,newC))
    return dis[N-1][N-1]


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dis = [[9999999] * (N) for _ in range(N)]

    print(f'#{tc} {solve()}')