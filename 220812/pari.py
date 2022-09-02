import sys
sys.stdin=open("pari.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())   # N * N 의 파리판
        # M * M 의 파리채

    pan = []
    for _ in range(N):
        lst = list(map(int, input().split()))
        pan.append(lst)


    maxpari = 0
    # while
    for y in range(N) :
        # maxpari = 0
        for x in range(N) :

            happari = 0
            for ym in range(M):
                for xm in range(M):

                    if y+M <=N and x+M <=N :
                        happari += pan[y+ym][x+xm]

            if happari > maxpari :
                maxpari = happari

                        # happari = pan[y+ym][x+xm]
                        # #
                        # # maxpari = 0
                        # if happari > maxpari :
                        #     maxpari = happari

            # if pan[y][x] + pan[y][x+1] + pan[y+1][x] + pan[y+1][x+1] > maxpari :
            #     maxpari = pan[y][x] + pan[y][x+1] + pan[y+1][x] + pan[y+1][x+1]

    print(f'#{tc} {maxpari}')


    # print(pan)
    # print(n)
    #     print(len(pan))
    # for x in range(len(pan))