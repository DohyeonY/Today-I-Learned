import sys
sys.stdin=open("sum.txt", "r")


T = 10

for tc in range(1, T+1) :
    tt = input()
    N = 100
    lst = [list(map(int, input().split())) for _ in range(N)]

    # col = 0
    # cross = 0
    # row = 0
    # recross = 0
    sumv = 0

    for i in range(N):
        
        
        recross = 0
        cross = 0
        col = 0
        row = 0
        # sumv = 0
        for j in range(N):
            col += lst[j][i] # 가로줄 합
            row += lst[i][j] # 세로줄 합
        # print(row)
            
            if sumv < col :
                sumv = col

            if sumv < row :
                sumv = row
                
            if i == j :
                cross += lst[i][i]   # 왼위 우아래 대각선 합
                recross += lst[i][N -1 -i]  # 왼아래 우위 역대각선 합
            # print(cross)

                if sumv < cross :
                    sumv = cross

                if sumv < recross :
                    sumv = recross
        
    print(f'#{tc} {sumv}')








