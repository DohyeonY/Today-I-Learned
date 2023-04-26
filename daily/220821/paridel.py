import sys
sys.stdin=open("pari.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())                    # N = 판의 크기  M = 파리채의 크기
    pan = [list(map(int, input(). split())) for _ in range(N)]   # N크기의 2차원 배열

    dr = [0, 0, 1, 1]                                           # 델타 기준값, 우측, 아래측, 대각선
    dc = [0, 1, 0, 1]
    maxpari = 0

    for row in range(N) :
        for col in range(N) :
            happari = 0                                          # 매번 4부위를 합할때마다 happari값을 초기화

            for i in range(M) :                                  # 파리채 row만큼의 크기
                for j in range(M) :                              # 파리채 col만큼의 크기
                    if 0<= row+i < N and 0<= col+j < N :
                        happari += pan[row+i][col+j]

            if maxpari < happari :                               # 최댓값 구하기
                maxpari = happari

    print(f'#{tc} {maxpari}')