import sys
sys.stdin=open("guganhap.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    N,M = map(int, input().split())
    ai = list(map(int, input().split()))
    # maxv = 0
    # minv = 999999999999

    maxv = 0
    minv = 99999999
    for i in range(0, N-M+1):
        sumv = 0

        for j in range(0, M):
            sumv += ai[i+j]
        if sumv > maxv :
            maxv = sumv
        if sumv < minv:
            minv = sumv

        # lst.append(sum(ai[i:i+M]))


    print(f'#{tc} {maxv - minv}')

    # for i in range(N-1, 0, -1): # 구간의 맨 끝 인덱스
    #     for j in range(i): # 인접원소 중 왼쪽원소 인덱스
    #         if ai[j] > ai[j+1]: # 오름차순, 더 큰수를 오른쪽으로
    #             ai[j], ai[j+1] = ai[j+1], ai[j]

                # print(ai)
            # minv = 0
            # maxv = 0
    # print(ai)
    # minv = 0
    # maxv = 0
    # for k in range(0,M):
    #     minv += ai[k]
    #     # print(k)
    # # print(minv)
    #
    # for y in range(N-1, N-M-1, -1):
    #     # print(y)
    #     maxv += ai[y]
    # # print(maxv)
    #
