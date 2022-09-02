import sys
sys.stdin=open("numofwords.txt", "r")

T = int(input())   # tc

for tc in range(1, T+1) :
    N = input()         # 첫 문자열
    M = input()         # 두번째 문자열

    # print(N, M)
    cnt = 0
    maxcnt = 0
    for i in range(len(N)) :
        for j in range(len(M)) :

            if N[i] == M[j] :
                cnt += 1

            if cnt > maxcnt :   # 초기화 전 maxcnt에 최대값 저장
                maxcnt = cnt
        cnt = 0             # N에 다른 값이 들어가면 카운트 초기화

    print(f'#{tc} {maxcnt}')