import sys
sys.stdin=open("화물도크.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = sorted(arr)
    # print(arr)
    cnt = 0
    # 끝나는 시간으로 내림차순 정렬
    arr.sort(key=lambda x: -x[1])
    # print(arr)
    # 끝나는 시간이 가장 짧은 것의 종료시간(정렬한 리스트의 가장 오른쪽 값 = 종료시간)
    endT = arr.pop()[1]
    # print(endT)
    # 화물이 빌때까지 반복
    while arr:
        s, e = arr.pop()
        # 이전화물끝나는 시간보다 늦게시작하면
        if endT <= s:
            # 엔드타임바꾸고  증가
            endT = e
            cnt += 1

    print(f'#{tc} {cnt + 1}')