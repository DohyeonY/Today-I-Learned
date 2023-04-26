import sys
sys.stdin=open("동철이의일분배.txt", "r")

def dfs(idx, s = 100) :
    global result
    if s <= result :
        return
    if idx >= N:
        result = s
        return
    for i in range(N):
        if visited[i]:
            visited[i] = 0
            dfs(idx+1, s * (arr[idx][i] / 100))
            visited[i] = 1

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] * N
    result = 0
    # print(arr)
    dfs(0)

    print(f'#{tc} {result:.6f}')