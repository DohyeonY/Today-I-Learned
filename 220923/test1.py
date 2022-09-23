# D4 2819 격자판의 숫자 이어 붙이기

import sys
sys.stdin=open("격자판.txt", "r")
# 상하좌우 이동 리스트
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for t in range(1, int(input()) + 1):
    numlist = [input().split() for _ in range(4)]
    # 중복을 없애기 위한 셋
    result = set()
    stack = []
    # 각자리마다 만들수 있는 수가 다르므로 각 자리마다 계산
    for i in range(4):
        for j in range(4):
            stack.append((i, j, 0, numlist[i][j]))
            while stack:
                y, x, count, ans = stack.pop()
                # 마지막인덱스까지 갔다면 결과 추가하기
                if count >= 6:
                    result.add(ans)
                    continue
                # 상하좌우 데이터 넣기
                for d_y, d_x, in move:
                    dy = d_y + y
                    dx = d_x + x
                    if 0 <= dy < 4 and 0 <= dx < 4:
                        stack.append((dy, dx, count + 1, ans + numlist[dy][dx]))
    print(result)
    print('#{} {}'.format(t, len(result)))