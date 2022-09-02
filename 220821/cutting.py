T = int(input())
for tc in range(1, T + 1):
    pack = input()

    stack = []
    cutnum = 0
    for i in range(len(pack)):
        if pack[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if pack[i - 1] == '(':
                cutnum += len(stack)
            else:
                cutnum += 1

    print(f'#{tc} {cutnum}')2
