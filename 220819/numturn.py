import sys
sys.stdin=open("numturn.txt", "r")



T = int(input())
# T = 1

for tc in range(1, T+1) :
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    # print(line)
    lst90 = [[[0] for _ in range(N)] for _ in range(N)]
    lst180 = [[[0] for _ in range(N)] for _ in range(N)]
    lst270 = [[[0] for _ in range(N)] for _ in range(N)]

    # print(lst90)
    for i in range(N) :                                 # 90도 회전
        for j in range(N) :
            # for _ in range(N) :
            lst90[i][j] = line[N-j-1][i]

    for i in range(N) :                                 # 180도 회전
        for j in range(N) :
            # for _ in range(N) :
            lst180[i][j] = lst90[N-j-1][i]

    for i in range(N) :                                 # 270도 회전
        for j in range(N) :
            # for _ in range(N) :
            lst270[i][j] = lst180[N-j-1][i]

    #
    # print(lst90)
    # print(lst180)
    # print(lst270)
    print(f'#{tc}')

    for k in range(N) :                                 # 출력 방법
        for t in range(N) :
            print(lst90[k][t], end='')
        print(end=' ')
        for t in range(N) :
            print(lst180[k][t], end='')
        print(end=' ')
        for t in range(N) :
            print(lst270[k][t], end='')
        print(end=' ')
        print()
