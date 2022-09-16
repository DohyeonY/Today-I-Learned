import sys
sys.stdin=open("오셀로.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    # N = 보드한변크기 M = 놓는 횟수
    N, M = map(int, input().split())
    # print(N, M)
    # 보드판 초기화
    board = [[0] * N for _ in range(N)]
    # print(board)

    # 시작판 설정
    startpoint = (N // 2) - 1
    board[startpoint][startpoint] = 2
    board[startpoint][startpoint + 1] = 1
    board[startpoint + 1][startpoint] = 1
    board[startpoint + 1][startpoint + 1] = 2
    # print(board)
    # 델타
    dr = [1, 0, -1, 0, 1, -1, 1, -1]
    dc = [0, 1, 0, -1, 1, -1, -1, 1]

    for _ in range(M) :
        C, R, Color = map(int, input().split())
        # print(C, R, Color)
        # 인덱스 0부터 시작이라 하나씩 빼주기
        C -= 1
        R -= 1
        # 돌 놓는 좌표 색칠
        board[R][C] = Color
        # 파리퇴치3과 같음
        for move in range(8) :
            for dis in range(1, N) :
                newR = R + (dr[move] * dis)
                newC = C + (dc[move] * dis)
                # 범위지정
                if 0 <= newR < N and 0 <= newC < N :
                    # 만약 빈 칸이면 스탑
                    if board[newR][newC] == 0 :
                        break
                    # 같은 색의 돌을 찾으면
                    elif board[R][C] == board[newR][newC] :
                        # 그 사이에 있는 모든 돌의 색을 바꿔줌
                        for i in range(1, dis) :
                            newnewR = R + (dr[move] * i)
                            newnewC = C + (dc[move] * i)
                            board[newnewR][newnewC] = Color
                        break

    # print(board)
    # 보드에서 검은색 흰색 돌을 카운트함수로 뽑아냄
    black = 0
    white = 0
    for k in range(N) :
        black += board[k].count(1)
        white += board[k].count(2)

    print(f'#{tc} {black} {white}')