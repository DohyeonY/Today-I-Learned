import sys
sys.stdin=open("세제곱근을찾아라.txt", "r")

# testcase
T = int(input())

for tc in range(1, T+1) :
    # 정수 입력
    N = int(input())
    # print(round(N ** (1/3)))
    if round(N ** (1/3)) ** 3 == N :
        print(f'#{tc} {round(N ** (1/3))}')
    else :
        print(f'#{tc} -1')
