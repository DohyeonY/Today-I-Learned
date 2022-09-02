N = int(input())   # 색종이의 갯수

dohwaji = [[0] * 101 for _ in range(101)]
lencolpaper = 10
for _ in range(N) :
    left, down = map(int, input().split())

    for row in range(10) :
        for col in range(10) :
            dohwaji[left + row][down + col] = 1
cnt = 0
# for row in dohwaji :
#     cnt += row.count(1)
for row in range(100) :
    for col in range(100) :
        if dohwaji[row][col] == 1 :
            cnt += 1
print(cnt)