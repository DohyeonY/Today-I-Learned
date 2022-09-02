import sys
sys.stdin=open("samsungbus.txt", "r")


T = int(input())                                       # testcase


for tc in range(1, T+1) :
    N = int(input())                                   # 노선의 갯수 N 입력
    Clen = [0] * 5001                                      # C의 범위만큼 빈 리스트 생성

    for _ in range(N) :
        A, B = map(int,input().split())                # 노선을 표현한 A,B 입력

        for i in range(A, B+1) :                       # A~B까지의 모든 노선을 Clen(빈리스트)에 각자 인덱스값에 저장

            Clen[i] += 1


    P = int(input())                                   # 정류장 갯수 입력

    result = []
    for _ in range(P) :                                # 정류장들 입력
        C = int(input())
        result.append(C)
        # print(C)
    # print(result)

    print(f'#{tc} ', end='')                           # Clen에 있는 정류장 인덱스값들을 뽑음
    for re in result :
        print(Clen[re],end=' ')
    print()