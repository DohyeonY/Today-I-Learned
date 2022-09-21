import sys
from tkinter import N
sys.stdin=open("최대상금.txt", "r")

def f(n, cnt):
    global maxV
    if n == cnt:
        tmp = int(''.join(num))
        if maxV < tmp:
            maxV = tmp
    else:
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                tmp = int(''.join(num))
                if tmp not in u[n]:
                    u[n].append(tmp)
                    f(n + 1, cnt)
                num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, T + 1):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    maxV = 0
    u = [[] for _ in range(10)]  # 중복 노드 방지
    f(0, cnt)
    print(f'#{tc} {maxV}')
    