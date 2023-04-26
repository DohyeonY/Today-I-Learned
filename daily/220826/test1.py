import sys
sys.stdin=open("중위순회.txt", "r")

TC = 10


def inord(root):
    if root != 0:
        inord(lst[root][1])
        print(lst[root][0], end='')
        inord(lst[root][2])


for tc in range(1, TC + 1):
    n = int(input())
    lst = [[0, 0, 0] for _ in range(n + 1)]

    for _ in range(n):
        tmp = list(input().split())

        lst[int(tmp[0])][0] = tmp[1]

        if len(tmp) == 3:
            lst[int(tmp[0])][1] = int(tmp[2])
        elif len(tmp) == 4:
            lst[int(tmp[0])][1] = int(tmp[2])
            lst[int(tmp[0])][2] = int(tmp[3])
    print(lst)
    print(f'#{tc} ', end='')
    inord(1)
    print()