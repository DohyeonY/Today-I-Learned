import sys
sys.stdin=open("triangle.txt", "r")

T = int(input())                # 테스트케이스

for tc in range(1, T+1) :
    N = int(input())            # 삼각형의 크기 N 입력
    result = []
    # lst = []
    for i in range(N) :
        lst = []                # 한 row만 만들고 리스트를 새로 리셋해줘야해서 여기다 넣어야함
        for j in range(i+1) :
            if j == 0 or j == i :   # 처음과 끝엔 항상 1이 들어가야함
                lst.append(1)

            else :         # 바로 윗 리스트의 자신과 x값이 같은거랑 x-1값이랑 더한게 아래에 있는값임
                lst.append(result[i-1][j] + result[i-1][j-1])

        result.append(lst)  # 이렇게 나온 하나의 row를 result에 append함
        # print(result)

    print(f'#{tc}')
    for k in result :
        print(*k)           # * : 리스트를 띄어쓰기만 유지한 상태로 출력



