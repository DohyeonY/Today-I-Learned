import sys
sys.stdin=open("보급로.txt")

from collections import deque

def solve() :
    Q = deque()
    Q.append((0, 0))
    recover[0][0] = 0
    while Q :
        row, col = Q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] :
            newR, newC = row + dy, col + dx
            if 0 <= newR < N and 0 <= newC < N :
                if recover[newR][newC] > recover[row][col] + arr[newR][newC] :
                    recover[newR][newC] = recover[row][col] + arr[newR][newC]
                    Q.append((newR,newC))
    return recover[N-1][N-1]


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    recover = [[9999999] * (N) for _ in range(N)]
    # solve()
    # print(recover[-1][-1])
    print(f'#{tc} {solve()}')