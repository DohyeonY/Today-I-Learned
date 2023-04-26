import sys
sys.stdin=open("oneandone.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, (input() + '0')))

    cnt = 0
    maxcnt = 0

    for i in lst:

        if i == 1:
            cnt += 1

        else:
            if maxcnt < cnt:
                maxcnt = cnt
                cnt = 0

    print(f'#{tc} {maxcnt}')