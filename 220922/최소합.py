import sys
sys.stdin=open("최소합.txt", "r",)
MAX = 999999999

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    # 아래줄에 절대 못가는 수를 한줄 추가하기 위해 일단 전부 MAX로 배열을 만들기
    arr = [[MAX for i in range(N + 1)] for j in range(N + 1)]
    for i in range(N):
        # 지도를 한행씩 입력받는다.
        temp = list(map(int, input().split()))
        arr[i] = temp
        # 오른쪽에 절대 못가는 수를 추가
        arr[i].append(MAX)
    # 도착지부터 역으로 돌기
    for row in range(N - 1, -1, -1):
        for col in range(N - 1, -1, -1):
            # 도착지는 스킵한다.
            if row == N - 1 and col == N - 1:
                continue
            # 현재 위치에서 오른쪽과 아래를 비교해 더 빠른 경로 찾기
            # 더 빠른 경로의 값을 현재 위치에 더해 갱신
            # 이렇게 하면 자연스레 모든 리스트의 값은 해당 위치에서 도착지까지의 최단경로값 형성
            if arr[row][col + 1] < arr[row + 1][col]:
                arr[row][col] = arr[row][col] + arr[row][col + 1]
            else :
                arr[row][col] = arr[row][col] + arr[row + 1][col]
    # 시작점에 구간의 최소값이 저장되니까 시작점을 출력
    print(f'#{tc} {arr[0][0]}')