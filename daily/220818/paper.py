import sys
sys.stdin=open("paper.txt", "r")

def cal(v) :                               # 계산 할 함수   cal(N) = cal(N-1) + (cal(N-2) * 2)

    if v == 1 :                             # N = 10일때 값 1
        return 1

    elif v == 2 :                           # N = 20일때 값 3   2개를 미리 설정해 주기
        return 3
    return cal(v-1) + (cal(v-2) * 2)


T = int(input())                            # testcase

for tc in range(1, T+1) :
    N = int(input())                        # 가로 크기 입력

    print(f'#{tc} {cal(N//10)}')            # N을 10으로 나눈 수로 계산해야해서 //10