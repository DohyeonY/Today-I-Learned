import sys
sys.stdin=open("boxchanger.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, Q = map(int, input().split())
    # print(N, Q)
    boxes = [0] * N

    for i in range(1, Q+1) :
        L, R = map(int, input().split())
        # print(L,R)
        for j in range(L-1, R) :
            boxes[j] = i
    print(f'#{tc} ', end='')
    for i in range(len(boxes)-1) :
        print(boxes[i], end=' ')
    print(boxes[-1])
