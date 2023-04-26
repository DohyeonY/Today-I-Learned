import sys
sys.stdin=open("bigyo.txt", "r")

T = int(input())  # tc

for tc in range(1, T+1) :
    N = input()        # 첫번째 문자열
    M = input()         # 두번째 문자열

    result = 0

    for i in range(len(M)-len(N)+1) :

        if N == M[i:i+len(N)] :
            result = 1

    print(f'#{tc} {result}')