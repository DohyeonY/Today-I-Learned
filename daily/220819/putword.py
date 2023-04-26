import sys
sys.stdin=open("putword.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    # print(ARR)
    result = 0
    #가로축의 갯수
    for row in range(N) :
        col = 0
        while col <= N-1 :
            while col <= N-1 and ARR[row][col] == 0 :
                col += 1
            cnt = 0
            while col <= N-1 and ARR[row][col] == 1 :
                col += 1
                cnt += 1
            if cnt == K :
                result += 1
    # print()
    # 세로축의 갯수
    for col in range(N) :
        row = 0
        while row <= N-1 :
            while row <= N-1 and ARR[row][col] == 0 :
                row += 1
            cnt = 0
            while row <= N-1 and ARR[row][col] == 1 :
                row += 1
                cnt += 1
            if cnt == K :
                result += 1

    print(f'#{tc} {result}')


for tc in range(1, T+1) :
    N, K = map(int, input().split())
    lst = [list(map(str, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N) :
        # 가로줄 검사
        row = ''.join(lst[i].split('0'))
        print(row)
        # if 