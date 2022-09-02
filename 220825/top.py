T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(input()) for _ in range(N+1)]

    for row in range(N) :
        for col in range(N) :
            if arr[row][col] == 'A' :
                k = 1

            if arr[row][col] == 'B' :
                k = 2

            if arr[row][col] == 'C' :
                k = 3

            # 각 방향별 k 만큼 확인
            for k in range(1, k+1) :
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)] :
                    if arr[row+dr*k][col+dc*k]

    # H의 수를 센다.
    for row in
        for col in