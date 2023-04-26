N = int(input())
dohwaji = [[0] * 1001 for _ in range(1001)]
a = 1
for k in range(1, N+1) :
    down, left, w, h = map(int, input().split())

    for i in range(down, down + w) :
        for j in range(left, left + h) :
            dohwaji[i][j] = k

cnt = [0] * (N+1)
for i in range(1001) :
    for j in range(1001) :
        if dohwaji[i][j] :
            cnt[dohwaji[i][j]] += 1

for i in range(1, N+1) :
    print(cnt[i])


# cnt = 0
# for row in range(1001) :
#     for col in range(1001) :
#         for color in range(N+1) :
#             a = dohwaji.count(color)


# print(dohwaji)