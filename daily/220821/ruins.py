import sys
sys.stdin=open("ruins.txt", "r")

for tc in range(int(input())):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    mx = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if lst[i][j] == 1:
                cnt += 1
                if mx < cnt :
                    mx = cnt
            else:
                cnt = 0


    for i in range(m):
        cnt = 0
        for j in range(n):
            if lst[j][i] == 1:
                cnt += 1
            else:
                if mx < cnt and cnt >= 2:
                    mx = cnt
                cnt = 0
        if mx < cnt and cnt >= 2:
            mx = cnt

    if mx < cnt and cnt >= 2:
        mx = cnt

    print(f'#{t + 1}', mx)
