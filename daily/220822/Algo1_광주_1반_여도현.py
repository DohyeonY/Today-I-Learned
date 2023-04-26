T = int(input())                                                            # testcase

for tc in range(1, T+1) :
    N = int(input())
    startrow, startcol, endrow, endcol = map(int, input().split())          # 왼쪽위 좌표와 오른쪽 아래 좌표
    arr = [list(map(int, input().split())) for _ in range(N)]               # 전체 영역 받아오기
    # print(arr)
    # print(startrow, endrow)
    # print(startcol, endcol)
    sumv = 0                                                                # 녹색영역의 총 숫자 합
    cntblock = 0                                                            # 영역의 갯수
    aver = 0                                                                # 평균값
    for row in range(startrow, endrow+1) :                                  # 녹색영역의 범위가 주어지기 때문에 N이 아닌 그걸 입력
        for col in range(startcol, endcol+1) :
            sumv += arr[row][col]
            cntblock += 1
    aver = sumv // cntblock                                                 # 평균값 구하기
    cnt = 0                                                                 # 몇 번 바꿨는지
    for row in range(startrow, endrow+1) :                                  # 녹색영역의 범위가 주어지기 때문에 N이 아닌 그걸 입력
        for col in range(startcol, endcol+1) :
            while arr[row][col] != aver :                                   # 평균보다 낮으면 더해서 올려주고
                if arr[row][col] < aver :
                    arr[row][col] += 1
                    cnt += 1
                elif arr[row][col] > aver :                               # 평균보다 높으면 빼서 내려줘서 평준화 시킴
                    arr[row][col] -= 1
                    cnt += 1

    # print(cnt)

    #         print(arr[row][col])
    #         print(row, col)

    print(f'#{tc} {cnt}')


