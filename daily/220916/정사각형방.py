import sys
sys.stdin=open("정사각형방.txt", "r")

T = int(input())
# 델타
dc = [0, 1, -1, 0]
dr = [1, 0, 0, -1]

for tc in range(1, T+1) :
    # 방의 크기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(lst)
    # 이동가능한지 체크용
    lst = [False] * (N * N + 1)
    maxcnt = 0
    cnt = 0
    minnum = 0
    for row in range(N) :
        for col in range(N) :
            for move in range(4) :
                newrow = row + dr[move]
                newcol = col + dc[move]
                # 이동 할 수 없으면 다른 방향으로 바꾸기
                if newrow < 0 or newrow >= N or newcol < 0 or newcol >= N :
                    continue
                # 이동 할 수 있으면 체크용 판에 트루 박기
                if arr[newrow][newcol] == arr[row][col] + 1 :
                    lst[arr[row][col]] = True
                    break
    # 체크용 판을 돌아가면서 확인 시작수가 가장 작은수여야 하니까 역으로 확인
    for i in range(N * N - 1, -1, -1) :
        # 만약 판이 트루면 카운트 +1
        if lst[i] == True:
            cnt += 1
        # 트루가 아니면 끊기는거니까 지금까지 추가한 카운트값을 저장 인덱스값도 저장 카운트 초기화
        elif lst[i] != True :
            if maxcnt <= cnt:
                maxcnt = cnt
                minnum = i + 1
            cnt = 0
    # 이동 할 수 없을때의 그 위치는 False라서 포함이 안되기 때문에 마지막에 하나 추가해줌
    maxcnt = maxcnt + 1

    print(f'#{tc} {minnum} {maxcnt}')


