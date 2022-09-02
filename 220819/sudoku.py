import sys
sys.stdin=open("sudoku.txt", "r")

T = int(input())                                            # testcase

for tc in range(1, T+1) :
    table = [list(map(int, input().split())) for _ in range(9)]
    comparelst = [1,2,3,4,5,6,7,8,9]                         # 얘랑 비교
    result = 1                                               # 기본값 1
    # print(table)

    for idx in range(9) :                                        # 가로 검사
        temp = table[idx][:]
        # print(temp)
        for i in range(len(temp) - 1, 0, -1):                # sort
            for j in range(i):
                if temp[j] > temp[j + 1]:
                    temp[j], temp[j + 1] = temp[j + 1], temp[j]
        if temp != comparelst :                              # sort 한 리스트가 비교군이랑 다르면 0으로

            result = 0
        # print(temp)
    # print(table)

    # print(turnd(table))

    for x in range(9) :                                         # 세로 검사
        col = []
        for y in range(9) :
            col.append(table[y][x])
        # print(col)
        for i in range(len(col) - 1, 0, -1):                 # sort
            for j in range(i):
                if col[j] > col[j + 1]:
                    col[j], col[j + 1] = col[j + 1], col[j]
        if col != comparelst :                              # 비교군이랑 sort한거랑 다르면 0
            result = 0
        # print(col)


    for i in range(9) :                                     # 3 x 3 검사
        for j in range(9) :
            # 9 x 9 판에서 3 x 3으로 분할 후 가장 왼쪽 위에 있는 구역을 기준으로 잡음
            if (i, j) == (0, 0)  or (i, j) == (0, 3) or (i, j) == (0, 6) or (i, j) == (3, 0) or (i, j) == (3, 3) or (i, j) == (3, 6) or (i, j) == (6, 0) or (i, j) == (6, 3) or (i, j) == (6, 6) :
                arr = []
                for k in range(3) :
                    for h in range(3) :
                        arr.append(table[i+k][j+h])
                # print(arr)
                for ii in range(len(arr) - 1, 0, -1):       # sort
                    for jj in range(ii):
                        if arr[jj] > arr[jj + 1]:
                            arr[jj], arr[jj + 1] = arr[jj + 1], arr[jj]
                if arr != comparelst:                       # 비교군이랑 sort한거랑 다르면 0
                    result = 0
                # print(arr)
    print(f'#{tc} {result}')






