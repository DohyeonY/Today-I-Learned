
def plus(a, b):
    return int(ary[a][0]) + int(ary[b][0])


def minus(a, b):
    return int(ary[a][0]) - int(ary[b][0])


def mul(a, b):
    return int(ary[a][0]) * int(ary[b][0])


def divi(a, b):
    return int(ary[a][0]) / int(ary[b][0])


TC = 1
for tc in range(1, TC + 1):
    node = int(input())
    ary = [0] * (node + 1)

    for _ in range(node):
        i, *value = input().split()

        ary[int(i)] = value
    print(ary)
    for j in range(node, 0, -1):
        if ary[j][0] == '-':
            ary[j][0] = minus(int(ary[j][1]), int(ary[j][2]))
        elif ary[j][0] == '+':
            ary[j][0] = plus(int(ary[j][1]), int(ary[j][2]))
        elif ary[j][0] == '*':
            ary[j][0] = mul(int(ary[j][1]), int(ary[j][2]))
        elif ary[j][0] == '/':
            ary[j][0] = divi(int(ary[j][1]), int(ary[j][2]))

    print(f'#{tc} {ary}')