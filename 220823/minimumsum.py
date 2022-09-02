import sys
sys.stdin=open("minimumsum.txt", "r")

def choiso(row, N, now_sum):
    global min_sum                                                                  # 최소합을 전역변수로 선언
    global visited
    if row == N:                                        # row                                            # 배열의 수와 일치하면
        if now_sum < min_sum:                                                       # 현재 합과 (지금까지)최소합 값을 비교
            min_sum = now_sum                                                       # 현재합이 더 작으면 대체

    elif now_sum > min_sum:                                                         # 현재 부분합이 더 크면 탐색 중지 (Pruning)
        return

    else:
        for col in range(N):
            if not visited[col]:                                                    # 방문 전인 컬럼
                visited[col] = 1                                                    # 방문처리
                choiso(row + 1, N, now_sum + arr[row][col])                # 다음 row로 넘어가고, now_sum에 값을 더해주고, visited 갱신
                visited[col] = 0                                                    # 함수 적용 후 초기화 (재검색 할 수 있도록)


T = int(input())                                                                    # testcase
for tc in range(1, T+1):
    N = int(input())                                                                # 줄의 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 999999999                                                             # 값을 대체해주기 임의의 큰 수 대입
    visited = [0] * N                                                               # 방문확인

    choiso(0, N, 0)
    print(f'#{tc} {min_sum}')