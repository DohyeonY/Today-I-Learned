import sys
sys.stdin=open("pari3.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())                            # N = 파리판의 크기 M = 파리채의 크기
    pan = [list(map(int, input().split())) for _ in range(N)]   # 파리판
    # print(pan)

    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]
    maxpari = 0                                                  # 최대로 많이 잡은 파리갯수
    for row in range(N) :
        for col in range(N) :

            happari = pan[row][col]                             # 중앙값은 항상 들어가게 초기화
            for i in range(4) :                                 # 상하좌우가 있는 델타값은 0~3인덱스 (방향값)
                for j in range(1, M) :                          # 파리채 크기만큼   (길이값)
                    R = row + dr[i] * j                         # 기준값 + 파리채 만큼의 길이를 전부 추가함
                    C = col + dc[i] * j

                    if 0 <= R < N and 0 <= C < N :
                        happari += pan[R][C]

            if maxpari < happari :
                maxpari = happari
                # print('1', row, col, happari)


            happari = pan[row][col]
            for i in range(4, 8) :                              # 대각선 4방향이 있는 델타값음 4~7인 인덱스
                for j in range(1, M) :
                    R = row + dr[i] * j
                    C = col + dc[i] * j

                    if 0 <= R < N and 0 <= C < N :
                        happari += pan[R][C]

            if maxpari < happari :
                maxpari = happari

    print(f'#{tc} {maxpari}')
