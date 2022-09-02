import sys
sys.stdin=open('miro.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(curR, curC) :
    visited = [[False] * N for _ in range(N)]
    ST = []
    # 1. 스택에 시작점을 push, 시작점 방문표시
    ST.append((curR, curC))
    visited[curR][curC] = True
    # 2. 스택에 데이타가 있는 동안
    while ST :
        curR, curC = ST.pop()
        # cur의 연결된 모든 포인트에 대하여
        for d in range(4) :
            newR = curR + dr[d]
            newC = curC + dc[d]
            # new 가 이동이 가능하면(선이 연결되어 있으면)
            # 방문 안했으면
            if 0 <= newR < N and 0 <= newC < N and miro[newR][newC] != 1 and not visited[newR][newC] :
                if miro[newR][newC] == 3 :
                    return 1
                ST.append((newR, newC))
                visited[newR][newC] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())                        # 미로의 가로세로 크기
    miro = [list(map(int, input())) for _ in range(N)] # 미로판 받기
    # print(miro)
    # 2를 찾기
    curC = 0
    curR = 0
    for row in range(N) :
        if miro[row].count(2) :
            curC = miro[row].index(2)
            curR = row

    print(f'#{tc} {dfs(curR, curC)}')

