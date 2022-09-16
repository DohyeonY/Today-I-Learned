import sys
sys.stdin=open("방범시스템.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    # 집만 리스트를 만들어라
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # print(N,M)
    savepoint = []
    for row in range(N) :
        for col in range(N) :
            if arr[row][col] == 1 :
                savepoint.append((row, col))
    # print(savepoint)
    maxhomes = 0
    for row in range(N) :
        for col in range(N) :
            checklst = [0] * (N * 2)
            for sr,sc in savepoint :
                dis = abs(row - sr) + abs(col - sc) + 1
                checklst[dis] += 1
            for i in range(1, len(checklst)) :
                checklst[i] += checklst[i - 1]
                if (checklst[i] * M) - (i**2 + (i - 1)**2) >= 0 :
                    if maxhomes < checklst[i] :
                        maxhomes = checklst[i]

    print(f'#{tc} {maxhomes}')