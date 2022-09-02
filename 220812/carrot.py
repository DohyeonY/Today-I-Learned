import sys
sys.stdin=open("carrot.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    l = len(carrot)
    cnt = 1
    maxcnt = 1

    for i in range(0, l-1):
        # print(i)
        # if i <= l-2 :

        if carrot[i] < carrot[i+1] :
            cnt += 1
            if maxcnt < cnt:
                maxcnt = cnt
#
        else:
            cnt = 1
    #
    print(f'#{tc} {maxcnt}')