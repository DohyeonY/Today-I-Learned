import sys
sys.stdin=open("방범시스템.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    # 집만 리스트를 만들어라
    # N = 가로세로 길이 M = 집당 줄수있는 인건비
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # print(N,M)
    # 집들의 위치를 튜플로 저장해 놓는다
    savepoint = []
    for row in range(N) :
        for col in range(N) :
            if arr[row][col] == 1 :
                savepoint.append((row, col))
    # print(savepoint)

    maxhomes = 0
    for row in range(N) :
        for col in range(N) :
            # arr의 좌표마다 체크리스트를 초기화함 체크리스트는 집과 좌표와의 거리들을 표시해줄것
            # 8*8 판에서 최대거리는 8 * N - 1인데 0인덱스는 무시하려고 +1 해줌
            checklst = [0] * (N * 2)
            # 원래 x좌표 - 집 x좌표 + 원래 y좌표 - 집 y좌표에다 본인 현재좌표도 거리1로 쳐서 +1해준게 거리값
            # 해당하는 체크리스트 인덱스에 집을 하나 씩 추가해준다
            for sr,sc in savepoint :
                dis = abs(row - sr) + abs(col - sc) + 1
                checklst[dis] += 1
            # 0은 사용하지 않으니 1부터 집의 최대거리값까지 돌린다
            for i in range(1, len(checklst)) :
                # 길이가 3이내인 집들은 1인집 + 2인집 + 3인집의 합이기때문에 이전 거리의 집들을 차곡차곡 더해준다
                checklst[i] += checklst[i - 1]
                # 유지비가 오버되면 안되기때문에 유지비 조건 추가
                if (checklst[i] * M) - (i**2 + (i - 1)**2) >= 0 :
                    # 맥스홈즈를 계속 갱신해준다
                    if maxhomes < checklst[i] :
                        maxhomes = checklst[i]

    print(f'#{tc} {maxhomes}')