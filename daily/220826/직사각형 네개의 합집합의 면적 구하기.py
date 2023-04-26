N = 4
arr = [[0] * 101 for _ in range(101)]
for _ in range(N) :
    dx, dy, ux, uy = map(int, input().split())

    for row in range(dx, ux) :
        for col in range(dy, uy) :
            arr[row][col] = 1

cnt = 0
for row in range(101) :
    for col in range(101) :

        if arr[row][col] :
            cnt += 1

print(cnt)