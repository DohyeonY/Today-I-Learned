import sys
sys.stdin=open("sudoku.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    arr = [list(map(int, input().split())) for _ in range(9)]                                # 스도쿠 판 9x9
    facnine = 1
    for i in range(1, 10) :                                                                 # 9! 구하는 코드
        facnine *= i
    # print(facnine)

    result = 1
    for i in range(9) :                                                                     # 가로줄 검사
        mulv = 1
        for j in range(9) :
            mulv *= arr[i][j]
        # print(mulv)
        if mulv != facnine :
            result = 0

    for i in range(9) :
        mulv = 1
        for j in range(9) :                                  # 세로줄 검사
            mulv *= arr[j][i]
            # print(mulv)
        if mulv != facnine :
            result = 0

    dr = [0, 1, 0, 1, 0, 1, 2, 2, 2]                                                       # 3x3용 델타값
    dc = [0, 0, 1, 1, 2, 2, 2, 0, 1]
    for i in range(9) :                                                               # 3x3 검사
        for j in range(9) :
            if (i, j) == (0, 0) or (i, j) == (0, 3) or (i, j) == (0, 6) or (i, j) == (3, 0) or (i, j) == (3, 3) or (i, j) == (3, 6) or (i, j) == (6, 0) or (i, j) == (6, 3) or (i, j) == (6, 6) :
                mulv = 1
                for k in range(9) :
                    mulv *= arr[i + dr[k]][j + dc[k]]
                    # print(mulv)
                if mulv != facnine :
                    result = 0

    print(f'#{tc} {result}')


