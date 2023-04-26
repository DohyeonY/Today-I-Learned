import sys
sys.stdin=open("최소생산비용.txt", "r")

def dfs(idx, s):
    global result
    if s >= result :
        return
    if idx == N:
        result = s
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx+1, s + arr[idx][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 9999999
    dfs(0,0)
    print(f'#{tc} {result}')