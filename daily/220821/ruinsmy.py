import sys
sys.stdin=open("ruins.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())                                        # N = 지도 가로길이 M = 세로길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)
    maxv = 0                                                                # 최대값 설정
    for row in range(N):
        cnt = 0                                                             # 가로줄이 끝나면 cnt 초기화
        for col in range(M):
            if arr[row][col] == 1:                                          # 만약 1이면 cnt하나씩 추가
                cnt += 1
                if maxv < cnt :                                             # 추가된 cnt를 maxv에 넣음
                    maxv = cnt
            else:                                                           # 만약 1이 아닌 0이라면 cnt는 초기화
                cnt = 0

    for col in range(M) :
        cnt = 0
        for row in range(N) :
            if arr[row][col] == 1 :
                cnt += 1
                if maxv < cnt :
                    maxv = cnt

            else :
                cnt = 0



    print(f'#{tc} {maxv}')
