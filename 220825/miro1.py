import sys
sys.stdin=open("miro1.txt", "r")

dr = [0, 0, 1, -1]                                                          # 델타값
dc = [1, -1, 0, 0]


def dfs(curR, curC):
    visited = [[False] * 16 for _ in range(16)]                               # visited 2차원배열
    Q = []
    # 1. 시작점을 push, 시작점 방문표시
    Q.append((curR, curC))
    visited[curR][curC] = True

    # 2. 데이타가 있는 동안
    while Q:
        #  Q의 데이터를 가져옴
        curR, curC = Q.pop(0)
        # cur의 연결된 4방향 포인트
        for d in range(4):
            newR = curR + dr[d]
            newC = curC + dc[d]
            # new 가 이동이 가능하면(선이 연결되어 있으면)
            # 방문 안했으면
            if 0 <= newR < 16 and 0 <= newC < 16 and miro[newR][newC] != 1 and not visited[newR][newC]:
                if miro[newR][newC] == 0:
                    # Q에 newRC를 넣어줌
                    Q.append((newR, newC))
                    # 거리를 나타내기 위해 visited에 계쏙 1씩 더해줌
                    visited[newR][newC] = visited[curR][curC] + 1
                    # miro의 현재 좌표는 1로 바꿔줌
                    miro[curR][curC] = 1
                # 도착점이라면
                elif miro[newR][newC] == 2 :
                    # visited의 현재 좌표의 거리값 -1 을 리턴(visited 현재값을 처음에 True로 설정해줬기 때문에 -1해줘야함)
                    return 1
    # 2를 찾지 못할때 0 리턴
    return 0


T = 10

for tc in range(1, T + 1):
    TC = int(input())  # 테스트케이스받기
    miro = [list(map(int, input())) for _ in range(16)]  # 미로판 받기
    # print(miro)
    # 3을 찾고 현재 좌표로 지정
    curC = 0
    curR = 0
    for row in range(16):
        for col in range(16) :
            if miro[row][col] == 3 :
                curR, curC = row, col
    #
    print(f'#{tc} {dfs(curR, curC)}')
