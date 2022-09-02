import sys
sys.stdin=open("coloring.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N = int(input())   # 칠할 영역의 갯수
    # cnt = 0
    n = 10
    rego = [[0] * n for _ in range(n)]
    # for z in range(N) :
    for _ in range(N) :
        r1, c1, r2, c2, color = map(int, input().split())  # 모서리 인덱스와 색상정보


        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1) :
                rego[r][c] += color # 빨강은 1을 더하구 파랑은 2를 더하구

        cnt = 0
        for l in range(n) :
            for m in range(n) :
                # print(rego)
                if rego[l][m] == 3 :
                    cnt += 1

    print(f'#{tc} {cnt}')
            # print(rego)
    # print(N)
    # print(K)


# 2차원 배열의 그림칠 / 같은 색 끼린 겹치지 않는다 / 000001111000002222211110000