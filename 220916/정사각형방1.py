import sys
sys.stdin=open("정사각형방.txt", "r")

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    # 옆으로 이동이 가능한지 체크하는 변수
    check_list = [False] * (N * N + 1)
    minnum = max_count = count = 0
    for i in range(N):
        for j in range(N):
            # 상하좌우를 이동해보며 이동이 가능한지 확인한다.
            for dy, dx in move_list:
                t_y = i + dy
                t_x = j + dx
                # 이동이 불가능하다면 다른방향을 확인한다.
                if t_y < 0 or t_x < 0 or t_y >= N or t_x >= N:
                    continue
                # 이동이 가능하다면 자신보다 1이큰지 확인한다.
                # 크다면 정지하고 다음을 확인
                if map_list[t_y][t_x] == map_list[i][j] + 1:
                    check_list[map_list[i][j]] = True
                    break
    # 연결되어있는 배열을 확인한다.
    for i in range(N * N - 1, -1, -1):
        # 연결이 되어있다면 카운트 증가
        if check_list[i]:
            count += 1
        # 연결이 끊겼다면 지금까지 누적된 카운트를 체크한다.
        elif count:
            # 최대 카운트보다 크다면 갱신하고 카운트 초기화
            if max_count <= count:
                max_count = count
                minnum = i + 1
            count = 0

    print("#{} {} {}".format(t, minnum, max_count + 1))


