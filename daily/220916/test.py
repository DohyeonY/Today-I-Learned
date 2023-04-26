import sys
sys.stdin=open("오셀로.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    board = [[0] * n for _ in range(n)]  # 보드 초기화

    init = n // 2 - 1
    board[init][init] = 2
    board[init][init + 1] = 1
    board[init + 1][init] = 1
    board[init + 1][init + 1] = 2
    print(board)
    # 델타 상하좌우 우상하 좌하상
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]

    # 하나 넣고 검사 반복
    for i in range(m):
        r, c, color = map(int, input().split())
        r -= 1
        c -= 1
        board[r][c] = color
        for j in range(8):  # 델타
            for d in range(1, n):  # 디스턴스
                if 0 <= r + (dr[j] * d) < n and 0 <= c + (dc[j] * d) < n:
                    if board[r + dr[j] * d][c + dc[j] * d] == 0:
                        break
                    elif board[r][c] == board[r + dr[j] * d][c + dc[j] * d]:
                        for k in range(1, d):
                            board[r + dr[j] * k][c + dc[j] * k] = color
                        break

    b = 0
    w = 0

    black = 0
    white = 0
    for k in range(n) :
        b += board[k].count(1)
        w += board[k].count(2)

    print(f'#{test_case} {b} {w}')