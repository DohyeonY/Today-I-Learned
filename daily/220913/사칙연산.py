def plus(a, b):                                             # 사칙연산 함수
    return int(arr[a][0]) + int(arr[b][0])
 
def sub(a, b):
    return int(arr[a][0]) - int(arr[b][0])
 
def mul(a, b):
    return int(arr[a][0]) * int(arr[b][0])
 
def div(a, b):
    return int(arr[a][0]) / int(arr[b][0])
 
T = 10                                                      # testcase
for tc in range(1, T+1) :   
    N = int(input())                                        # 정점의 갯수
    arr = [0] + [input().split() for _ in range(N)]         # 정점의 갯수 +1 만큼 배열 생성

    # print(arr)
    for i in range(1, N+1) :                                # 의미 없는 노드번호 제거
        del arr[i][0]

    # print(arr)
    for i in range(N, 0, -1) :                              # 뒤에서부터 탐색
        if arr[i][0] == '+' :                               # 만약 index 0번에 사칙연산 중 하나의 기호가 나오면
            arr[i][0] = plus(int(arr[i][1]), int(arr[i][2]))# index 1번과 2번에 해당하는 노드의 값들로 사칙연산 실행 후 기호를 대체함

        elif arr[i][0] == '-' :
            arr[i][0] = sub(int(arr[i][1]), int(arr[i][2]))

        elif arr[i][0] == '*' :
            arr[i][0] = mul(int(arr[i][1]), int(arr[i][2]))

        elif arr[i][0] == '/' :
            arr[i][0] = div(int(arr[i][1]), int(arr[i][2]))

    print(f'#{tc} {int(arr[1][0])}')