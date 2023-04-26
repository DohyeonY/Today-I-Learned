import sys
sys.stdin=open("fastest.txt", "r")

T = int(input())    # tc

for tc in range(1, T+1) :
    N, M = input().split()          # N = 문자열 A  M = 문자열 B

    # print(N, M)
    cnt = 0
    a = 0
    i = 0

    # for i in range(len(N) - len(M) + 1) :
    while i < len(N) :
        if N[i] == M[0] :
            if M == N[i:i+len(M)] :
                cnt += 1
                i += len(M)

            else :
                cnt += 1
                i += 1

        else :
            cnt += 1
            i += 1

    # print(cnt)





    # print(cnt)

    # a = len(N) - (len(M) -1) * cnt   # N과 M의 길이에 따른 공식
    #
    print(f'#{tc} {cnt}')