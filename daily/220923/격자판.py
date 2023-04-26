import sys
sys.stdin=open("격자판.txt", "r")

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, T+1) :
    arr = [input().split() for _ in range(4)]
    # print(arr)
    result = set()
    lst = []
    for row in range(4) :
        for col in range(4) :
            lst.append((row, col, 0, arr[row][col]))
            while lst:
                y, x, cnt, ans = lst.pop()
                # 마지막인덱스까지 갔다면 결과 추가하기
                if cnt >= 6:
                    result.add(ans)
                    continue
                # 상하좌우 데이터 넣기
                # for drow, dcol in move:
                #     d\ = d_y + y
                #     dx = d_x + x
                #     if 0 <= dy < 4 and 0 <= dx < 4:
                #         lst.append((dy, dx, cnt + 1, ans + arr[dy][dx]))
                for i in range(4) :
                    newrow = y + dr[i]
                    newcol = x + dc[i]
                    if 0 <= newrow < 4 and 0 <= newcol < 4 :
                        lst.append((newrow, newcol, cnt + 1, ans + arr[newrow][newcol]))

    print(f'#{tc} {len(result)}')