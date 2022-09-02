import sys
sys.stdin=open("달란트.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, P = map(int,input().split())                 # N = 달란트 P = 묶음수
    # print(N, P)
    result = 0
    if N % P == 0 :                                 # 달란트가 묶음수로 나누어 떨어질때
        a = N // P
        result = a**P

    else :
        result = (((N // P)+1)**(N % P)) * ((N // P)**(P - (N % P)))

    print(f'#{tc} {result}')
