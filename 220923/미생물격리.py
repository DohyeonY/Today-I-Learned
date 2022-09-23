import sys
sys.stdin=open("미생물격리.txt", "r")

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

T = int(input())

for tc in range(1, T+1) :
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M) :
        for i in range(len(arr)) :
            row, col, num, dir = arr[i]
            if not num :                                            # if k의 미생물이 0이면 : continue
                continue
            newrow = row + dr[dir]
            newcol = col + dc[dir]
            arr[i][0], arr[i][1] = newrow, newcol               # 좌표이동
            if not (1 <= newrow < N-1 and 1 <= newcol < N-1) :      # 벽이면
                arr[i][2] = arr[i][2] // 2                      # 미생물값을 반으로
                arr[i][3] = rev[dir]                              # 방향 전환
        arr.sort()
        pre = 0
    # print(arr)
        for i in range(1, K) :
            if arr[i][2] == 0 :
                continue
            if arr[i][0] == arr[pre][0] and arr[i][1] == arr[pre][1] :
                arr[i][2] += arr[pre][2]                             # arr[k]에 미생물 내용에 누적
                arr[pre][2] = 0
            pre = i                                                  # pre는 0

    # print(arr)
    result = 0
    for k in arr :
        result += k[2]

    print(f'#{tc} {result}')
