import sys
sys.stdin=open("puzzle.txt", "r")

T = int(input())
# T = 1
for tc in range(1, T+1) :
    N, K = map(int, input().split())                                    # N = 판 크기 K = 찾아야하는 글자 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    sumk = 0                                                            # 글자가 들어갈수있는 공간의 갯수

    for row in range(N) :                                               # 가로검사
        cnt = 0                                                         # 초기화
        for col in range(N) :
            if arr[row][col] == 1 :                                     # 만약 1이면 cnt를 하나 씩 늘린다
                cnt += 1

            else :                                                      # 아닐땐 cnt가 3이면 1개의 완성이라 sumk를 늘리고 cnt를 초기화
                if cnt == K :                                           # 1이 아닐때만 체크해야지 1일때 바로 체크하면 4개 5개칸이 있는곳도 카운팅이 되어버림
                    sumk += 1
                    cnt = 0
                else :                                                  # 아니고 cnt도 3이 아니면 그냥 초기화
                    cnt = 0
        if cnt == K :                                                   # 마지막줄에 1이 나오면 체크가 안되어서 col이 한바퀴 도는 곳에도 한번 더 체크 후 초기화
            sumk += 1



    for col in range(N) :
        cnt = 0
        for row in range(N) :
            if arr[row][col] == 1 :
                cnt += 1
            else :
                if cnt == K :
                    sumk += 1
                    cnt = 0
                else :
                    cnt = 0
        if cnt == K :
            sumk += 1

    print(f'#{tc} {sumk}')