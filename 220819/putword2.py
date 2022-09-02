import sys
sys.stdin=open("putword.txt", "r")

T = int(input())                                            # testcase

for tc in range(1, T+1) :
    N, K = map(int, input().split())
    lst = [list(map(str, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N) :

        row = ''.join(lst[i]).split('0')                    # 가로줄 검사
        # print(row)
        for r in row:
            if '1' * K == r:                                 # 만약 1이 K만큼 row에 있으면 카운트에 1추가
                cnt += 1
        # print(cnt)

        colr = ''

        for j in range(N) :
            colr += lst[j][i]                                # 세로줄 검사

        col = colr.split('0')
        # print(col)
        for c in col :
            if '1' * K == c :                                 # 만약 1이 K만큼 col에 있다면 카운트에 1추가
                cnt += 1

    print(f'#{tc} {cnt}')