import sys
sys.stdin=open("hoimun.txt", "r")

T = int(input())   # tc

for tc in range(1, T+1):
    N, M = map(int, input(). split())   # N = 판크기 M = 동일한 글자 수

    pan = []
    for _ in range(N) :
        lst = input()
        pan.append(lst)

    # print(pan)
    a = ''
    for i in range(N) :
        for j in range(N-M+1) : # 1,2케이스면 0만 3케이스면 0~8까지
            panx = []
            pany = []
            for k in range(M) :  # 1,2케이스면 1~9  3케이스면 0~11
                panx.append(pan[i][j+k])
                pany.append(pan[j+k][i])

            if panx == panx[::-1] :
                a = "".join(panx)
            if pany == pany[::-1] :
                a = "".join(pany)





            # print(pan[y][M-1])
            # if pan[y][0:M] == pan[y][M-1:0] :
            #     a = pan[y][0:M]
            # if pan[0:M][x] == pan[::-1][x] :
            #     a = pan[::][x]



    print(f'#{tc} {a}')